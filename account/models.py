from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.contrib.auth import get_user_model



class User(AbstractBaseUser, PermissionsMixin):
    email         = models.EmailField(_('email address'), unique=True)
    user_name     = models.CharField(max_length=150, verbose_name="username", unique=True)
    first_name    = models.CharField(max_length=150, blank=True)
    last_name     = models.CharField(max_length=150, blank=True)
    date_joined   = models.CharField(default=timezone.now, max_length=40)
    is_staff      = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD   = 'email'
    REQUIRED_FIELDS  = ['user_name', 'first_name', 'last_name']

    def __str__(self):
        return self.user_name


