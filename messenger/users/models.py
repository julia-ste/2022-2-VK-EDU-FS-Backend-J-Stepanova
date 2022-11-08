from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    town = models.CharField(max_length=30, blank=True)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
