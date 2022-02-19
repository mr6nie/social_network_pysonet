from django.db import models
from django.contrib.auth import get_user_model

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from apps.comments.models import AbstractComment

User = get_user_model()


class Post(models.Model):
    """Посты"""

    text = models.TextField(max_length=1024)
    create_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    moderation = models.BooleanField(default=True)
    view_count = models.PositiveBigIntegerField(default=0)
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)

    def __str__(self):
        return f"Post by {self.user}"

    def comments_count(self):
        return self.comments.count()


class Comment(AbstractComment, MPTTModel):
    """Модель коментариев к постам"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    parent = TreeForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
    )

    def __str__(self):
        return "{} - {}".format(self.user, self.post)
