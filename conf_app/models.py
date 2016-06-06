from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, UserManager


class Company(models.Model):
    name = models.CharField(max_length=80)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)


class CustomUser(User):
    userpic = models.ImageField(upload_to='userpics/', blank=True, null=True)
    company = models.ForeignKey(Company, blank=True, null=True)
    objects = UserManager()


class Event(models.Model):
    title = models.CharField(max_length=80)
    address = models.CharField(max_length=150)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()
    members = models.ManyToManyField(CustomUser, through="Participant", blank=True)
    sponsors = models.ManyToManyField(Company, blank=True)


class Participant(models.Model):
    LISTENER = "LS",
    SPEAKER = "SP"
    ROLES = (
        (LISTENER, 'Listener'),
        (SPEAKER, 'Speaker')
    )
    user = models.ForeignKey(CustomUser)
    event = models.ForeignKey(Event)
    role = models.CharField(max_length=2, choices=ROLES, default=LISTENER)

