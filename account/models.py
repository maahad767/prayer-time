from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from account.validators import bsid_validator, phone_validator


class OfficeLocation(models.Model):
    branch = models.CharField(max_length=50)
    floor = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.branch} {self.floor}"


class User(AbstractUser):
    bsid: str = models.CharField(
        max_length=6,
        blank=True,
        null=True,
        validators=[bsid_validator],
        verbose_name=_("BSID"),
        help_text=_("BSID must be valid BSID(BSXXXX)"),
    )

    phone: str = models.CharField(
        max_length=14,
        blank=True,
        null=True,
        validators=[phone_validator],
        verbose_name=_("Phone"),
        help_text=_("Phone must be valid Bangladeshi phone number"),
    )

    office_location = models.ForeignKey(
        OfficeLocation,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_("Office Location"),
    )

    def __str__(self):
        return self.username
