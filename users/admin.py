from django.contrib import admin
from .models import UserModel, ProfileModel
# Register your models here.

admin.site.register(UserModel)
admin.site.register(ProfileModel)