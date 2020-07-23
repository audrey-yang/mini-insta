from django.urls import path
from . import views
app_name = "instagram"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('like/<int:id>', views.like, name='like'),
    path('make-post', views.post, name='make-post'),
    path('my-posts', views.MyPostsView.as_view(), name='my-posts'),
    path('my-posts/delete/<int:id>', views.delete, name='delete'),
    path('profile/<int:id>', views.profile, name='profile'),
    #path('profile/edit/', views.edit_profile, name='edit-profile'),
    path('register', views.register, name='register'),
    path('logout', views.logout_request, name='logout'),
    path('login', views.login_request, name="login")
] 