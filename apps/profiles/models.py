from django.db import models
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField


# class UserNet(AbstractUser):
#     """custom user model"""

#     middle_name = models.CharField(max_length=50, blank=True, null=True)
#     first_login = models.DateTimeField(null=True)
#     phone = PhoneNumberField()
#     avatar = models.ImageField(upload_to="user/avatar")
