# Generated by Django 4.1.3 on 2022-11-22 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chats", "0004_message_is_read"),
    ]

    operations = [
        migrations.AddField(
            model_name="chatmember",
            name="is_admin",
            field=models.BooleanField(default=False, verbose_name="Админ"),
        ),
    ]
