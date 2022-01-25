from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.contrib.auth import get_user_model



class User(AbstractBaseUser, PermissionsMixin):
    username      = models.CharField(max_length=30, unique=True, null=True)
    is_verified   = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=True)
    date_joined   = models.DateTimeField(default=timezone.now)


    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


