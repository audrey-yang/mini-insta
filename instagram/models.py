from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published', default=None) 
    numLikes = models.IntegerField(default=0)
    likedUsers = models.CharField(max_length=1000, default="")
    def __str__(self):
        return self.text