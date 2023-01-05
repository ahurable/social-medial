from django.db import models
from django.contrib.auth import get_user_model

from random import randint
from datetime import datetime

import os
# Create your models here.

User = get_user_model()

def img_upload(instance, path):

    rand_int  =  randint(1000000, 999999999)
    file_name =  os.path.basename(path)
    ex_name, ext = os.path.splitext(file_name)
    today = datetime.date(datetime.today())
    save_path = f"posts/img/{today}/{rand_int}{ext}"
    return save_path

class Post(models.Model):

    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to=img_upload, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    likes = models.ManyToManyField(User, blank=True, related_name='likes')

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self) -> str:
        return self.title



class Comment(models.Model):

    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self) -> str:
        return f"{self.author} {self.post}"
    
