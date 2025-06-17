from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    twitter_username = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True)
    birthdate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username
