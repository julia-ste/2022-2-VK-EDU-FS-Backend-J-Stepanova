from application.settings import AUTH_USER_MODEL
from django.db import models

from users.models import User


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Chat(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_group = models.BooleanField(default=False)
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name="user_chats"
    )
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        related_name="category_chats"
    )

    def __str__(self):
        return self.title


class ChatMember(models.Model):
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name="chat_chat_members"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_chat_members"
    )
    joined_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["chat", "user"]


class Message(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="author_messages",
    )
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name="chat_messages",
    )
    text = models.CharField(max_length=4096)
    sent_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
