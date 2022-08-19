from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import Signal


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="profile")
    address = models.CharField(blank=True, null=True,max_length=150)
    phone_number = models.CharField(max_length=14)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"

def delete_user(sender, instance, **kwargs):
       profile = instance
       user = profile.user
       user.delete()

Signal.connect(post_delete, delete_user,sender=Profile)