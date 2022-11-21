from django.db import models

from application.settings import AUTH_USER_MODEL


class Category(models.Model):
    title = models.CharField("Название", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Chat(models.Model):
    title = models.CharField("Название", max_length=50)
    description = models.TextField("Описание", null=True, blank=True)
    is_group = models.BooleanField("Чат", default=False)
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name="user_chats",
        verbose_name="Автор"
    )
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="category_chats",
        verbose_name="Категория"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"


class ChatMember(models.Model):
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        verbose_name="Чат"
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    joined_at = models.DateTimeField("Дата присоединения", auto_now=True)

    def __str__(self):
        return f"{self.chat} - {self.user}"

    class Meta:
        unique_together = ["chat", "user"]
        verbose_name = "Участник чата"
        verbose_name_plural = "Участники чата"


class Message(models.Model):
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="author_messages",
        verbose_name="Автор"
    )
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name="chat_messages",
        verbose_name="Чат"
    )
    text = models.CharField("Текст", max_length=4096)
    sent_at = models.DateTimeField("Дата отправления", auto_now=True)
    is_read = models.BooleanField("Прочитано", default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ['-sent_at']
