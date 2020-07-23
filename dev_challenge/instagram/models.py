from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    image = models.ImageField(default="default.png")
    text = models.CharField(default="", blank=True, max_length=100)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    numLikes = models.IntegerField(default=0)
    likedUsers = models.CharField(max_length=1000, default="")
    def __str__(self):
        return self.text

class Profile(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    prof_pic = models.ImageField(default="default.png", blank=True)
    bio = models.CharField(default="", blank=True, max_length=100)
    def __str__(self):
        return self.user.username