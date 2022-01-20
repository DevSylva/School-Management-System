from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):

        if not email:
            raise TypeError(_('The Email must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.is_student = True
        user.save()

        return user

    def create_staff(self, email, password=None):
        if not email:
            raise TypeError("The Email must be set.")

        user = self.create_user(email, password)
        user.is_staff = True
        user.save()

        return user

    def create_superuser(self, email, password=None):

        if password is None:
            raise TypeError('Passwords should not be None')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_verified = True
        user.is_staff = True
        user.is_student = True
        user.save()

        return user
