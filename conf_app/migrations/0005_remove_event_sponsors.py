# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-12 01:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conf_app', '0004_auto_20160612_0442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='sponsors',
        ),
    ]
