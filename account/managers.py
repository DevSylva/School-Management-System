from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None):

        if not username:
            raise ValueError("User must posses a Username.")

        # username = self.normalize_email(email)
        user = self.model(username=username)
        user.set_password(password)
        user.save()

        return user


    def create_superuser(self, username, password=None):

        if password is None:
            raise TypeError('Passwords should not be None')

        user = self.create_user(username, password)
        user.is_superuser = True
        user.save()

        return user
