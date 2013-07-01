from __future__ import unicode_literals

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin,
    UserManager, AnonymousUser)
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    A thin wrapper around the default BaseUserManager
    """
    def create_user(self, email=None, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        pass

    def create_superuser(self, email, password):
        pass


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Our custom user
    """
    username = something
