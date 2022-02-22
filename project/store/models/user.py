from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AnonymousUser

from typing import Any, Union

from project.store.models.abstracts import TimeStampedModel
from project.store.utils import PathAndRename
from project.store.managers import UserManager


class User(AbstractBaseUser,PermissionsMixin,TimeStampedModel):
    """
    override the user database model to login with email instead of username
    """
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login : Any = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to = PathAndRename('user/avatar/'))

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self) -> str:
        return str(self.email)

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm : str , obj:Union[models.Model, AnonymousUser, None]=None) -> bool:
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    @staticmethod
    def has_module_perms(app_label : Any) -> bool:
        return True