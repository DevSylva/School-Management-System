from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Student(models.Model):

    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    # user            = models.ForeignKey(to=User, on_delete=models.CASCADE)
    first_name      = models.CharField(max_length=16, blank=True)
    last_name       = models.CharField(max_length=16, blank=True)
    reg_number      = models.CharField(max_length=8, verbose_name="Registration Number", blank=True, unique=True)
    gender          = models.CharField(choices=GENDER, default="Male", max_length=6)
    phone_number    = models.CharField(max_length=16, null=True, blank=True)
    created_at      = models.CharField(default=timezone.now, max_length=40)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'reg_number']


    def __str__(self):
        return f"{self.first_name} {self.last_name}"