from django.utils.translation import ugettext as _
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class MyUser(AbstractBaseUser):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=200, blank=False, null=False,
        help_text=_('A string describing the MyModel title.'))

    username = models.CharField(
        verbose_name=_('username'),
        max_length=150,
        unique=True,
        error_messages={
            'unique': _("A user with that username already exists.")
        }
    )

    USERNAME_FIELD = 'username'
