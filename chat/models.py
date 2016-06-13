from __future__ import unicode_literals

from django.db import models
from swampdragon.models import SelfPublishModel

from chat.serializers import ChatSerializer, MessageSerializer
from conf_app.models import CustomUser


class Chat(models.Model):
    serializer_class = ChatSerializer
    title = models.CharField(max_length=30)
    users = models.ManyToManyField(CustomUser)


class Message(SelfPublishModel, models.Model):
    serializer_class = MessageSerializer
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    chat = models.ForeignKey(Chat)
    author = models.ForeignKey(CustomUser)


class Notification(models.Model):
    name = models.CharField(max_length=100)
