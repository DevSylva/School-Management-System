from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.contrib.auth import get_user_model



class User(AbstractBaseUser, PermissionsMixin):


    email = models.EmailField(_('email address'),unique=True)
    is_staff = models.BooleanField(default=True)
    is_student = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['is_staff', 'is_student']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Staff(models.Model):

    User = get_user_model()

    GENDER = (
        ("M", "MALE"),
        ("F", "FEMALE"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER, max_length=1)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user

    def get_full_name(self):
        return f"{first_name} {middle_name} {last_name}"

