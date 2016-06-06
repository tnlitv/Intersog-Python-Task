from __future__ import unicode_literals

from django.db import models
from conf_app.models import CustomUser


class Post(models.Model):
    title = models.CharField(max_length=80)
    text = models.TextField()
    author = models.ForeignKey(CustomUser, limit_choices_to={'is_superuser': True})
    created_at = models.DateTimeField(auto_now_add=True, editable=False)


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(CustomUser)
    text = models.TextField()
