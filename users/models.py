from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.models import UserManager
from django.conf import settings

import os
from datetime import datetime
from random import randint
# Create your models here.

class UserManager(UserManager):

    def create_superuser(self, username: str, email, password, **extra_fields):
        return super().create_superuser(username, email, password, **extra_fields)

    def create_user(self, username: str, email, password, **extra_fields):
        return super().create_user(username, email, password, **extra_fields)

class UserModel(AbstractUser, PermissionsMixin):

    name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=80)
    phone_number = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=12)

    objects = UserManager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

def img_upload(instance, path):

    rand_int  =  randint(1000000, 999999999)
    file_name =  os.path.basename(path)
    ex_name, ext = os.path.splitext(file_name)
    today = datetime.date(datetime.today())
    save_path = f"users/img/{today}/{rand_int}{ext}"
    return save_path


class ProfileModel(models.Model):

    profile_picture = models.ImageField(upload_to=img_upload, default="users/img/UserDefaultPicture.webp", null=True, blank=True)
    about  = models.TextField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followers")
    followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings")

    def __str__(self) -> str:
        return self.user.username + "'s profile"