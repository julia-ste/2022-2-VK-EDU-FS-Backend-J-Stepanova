from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    town = models.CharField(max_length=30, blank=True)
    birthday = models.DateField(null=True, blank=True)

    def get_fullname(self):
        return f"{self.last_name} {self.first_name}"

    def __str__(self):
        return self.get_fullname()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
