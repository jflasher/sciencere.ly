from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    url = models.URLField("Website", blank=True)
    institution = models.CharField(max_length=50, blank=True)