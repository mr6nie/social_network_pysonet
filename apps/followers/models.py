from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Follower(models.Model):
    """Модель подписчиков"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    subscriber = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower"
    )
