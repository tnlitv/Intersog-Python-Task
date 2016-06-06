from __future__ import unicode_literals

from django.db import models
from conf_app.models import CustomUser


class Chat(models.Model):
    title = models.CharField(max_length=30)
    users = models.ManyToManyField(CustomUser)


class Message(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    chat = models.ForeignKey(Chat)
