from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .customusermanagers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    state = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        verbose_name=_('State'),
    )
    city = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        verbose_name=_('City'),
    )
    address = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Address"),
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email