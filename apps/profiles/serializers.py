from dataclasses import fields
from rest_framework import serializers

from .models import UserNet


class GetUserNetSerializer(serializers.ModelSerializer):

    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserNet
        exclude = (
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
        )


class GetUserNetPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNet
        exclude = (
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
            "email",
            "phone",
        )


class UserByFollowerSerializer(serializers.ModelSerializer):
    """сериализация для подписчиков"""

    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserNet
        fields = (
            "id",
            "username",
            "avatar",
        )
