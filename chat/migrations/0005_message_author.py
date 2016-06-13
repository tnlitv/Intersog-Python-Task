# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conf_app', '0006_event_sponsors'),
        ('chat', '0004_remove_chat_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='author',
            field=models.ForeignKey(default=1, to='conf_app.CustomUser'),
            preserve_default=False,
        ),
    ]
