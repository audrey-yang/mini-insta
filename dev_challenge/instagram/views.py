from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
import datetime

from .models import Post, Profile
from .forms import RegisterForm, MakePostForm
from django.contrib.auth.models import User
from django.contrib import messages

# POSTS
class IndexView(generic.ListView):
    template_name = 'instagram/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')

class MyPostsView(generic.ListView):
    template_name = 'instagram/my-posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(
            author=self.request.user
        ).order_by('-pub_date')

def delete(request, id):
    get_object_or_404(Post, pk=id).delete()
    return redirect("instagram:my-posts")

def like(request, id):
    post_to_like= get_object_or_404(Post, pk=id)
    user = request.user.username 
    liked = user + "," in post_to_like.likedUsers
    if liked:
        post_to_like.numLikes -= 1
        post_to_like.likedUsers = post_to_like.likedUsers.replace(user + ",", "")
    else:
        post_to_like.numLikes += 1
        post_to_like.likedUsers += user + ","
    post_to_like.save()
    return redirect("instagram:index")

def post(request):
    if request.method == "POST":
        form = MakePostForm(request.POST, request.FILES)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            now = datetime.datetime.now()
            image = request.FILES['image'];
            new_post = Post(author=request.user, image=image, text=text, pub_date=now)
            new_post.save()
            return redirect("instagram:index")
        else:
            
            messages.info(request, "Error: Form is not valid!" + form._errors)
            return redirect("instagram:index")
    form = MakePostForm
    return render(request = request,
                  template_name = "instagram/make-post.html",
                  context = {"form":form})

# PROFILE
def profile(request, id):
    user = get_object_or_404(User, pk=id)
    user_prof = Profile.objects.get(user=user)
    return render(request = request, 
                    template_name = "instagram/profile.html", 
                    context = {"profile": user_prof})

def edit_profile(request, id):
    pass

#LOGIN
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(user=user)
            profile.save()
            login(request, user)
            return redirect("instagram:index")
        else:
            print(form._errors);
            messages.info(request, form._errors)            
            return render(request = request,
                          template_name = "instagram/register.html",
                          context = {"form":form})
    form = RegisterForm
    return render(request = request,
                  template_name = "instagram/register.html",
                  context = {"form":form})

def logout_request(request):
    logout(request)
    return redirect("instagram:index")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('instagram:index')
            else:
                messages.info(request, "Invalid username or password")
        else:
            messages.info(request, form._errors)   
            print("Invalid username or password")
    form = AuthenticationForm()
    return render(request = request, 
                  template_name = "instagram/login.html", 
                  context = {"form":form})