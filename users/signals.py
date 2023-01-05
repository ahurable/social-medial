from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from .models import ProfileModel, UserModel

@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ProfileModel.objects.create(user=instance)