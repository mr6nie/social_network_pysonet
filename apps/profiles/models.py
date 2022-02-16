from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField


class UserNet(AbstractUser):
    """custom user model"""

    GENDER = (
        ("male", "male"),
        ("female", "female"),
        ("other", "other"),
    )

    middle_name = models.CharField(
        _("middle name"), max_length=50, blank=True, null=True
    )
    first_login = models.DateTimeField(_("first login"), null=True)
    phone = PhoneNumberField(_("phone number"), unique=True)
    avatar = models.ImageField(
        _("avatar"), upload_to="user/avatar", blank=True, null=True
    )
    bio = models.TextField(blank=True, null=True)
    github = models.CharField(max_length=500, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default="other")
