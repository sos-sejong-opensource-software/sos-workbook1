from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_id = models.CharField(max_length=50, unique=True, default="user_id")
    hobby = models.CharField(max_length=50, null=True)


