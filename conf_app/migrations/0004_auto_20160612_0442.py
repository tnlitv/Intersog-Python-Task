# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-12 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conf_app', '0003_auto_20160612_0441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='member',
        ),
        migrations.RemoveField(
            model_name='event',
            name='sponsor',
        ),
        migrations.AddField(
            model_name='event',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='members_set', through='conf_app.Participant', to='conf_app.CustomUser'),
        ),
        migrations.AddField(
            model_name='event',
            name='sponsors',
            field=models.ManyToManyField(blank=True, related_name='sponsors_set', to='conf_app.CustomUser'),
        ),
    ]