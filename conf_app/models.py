from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, UserManager

from chat.serializers import CustomUserSerializer


class CustomUser(User):
    serializer_class = CustomUserSerializer

    COMPANY = 'C'
    USER = 'U'
    ROLES = [
        ('U', 'User'),
        ('C', 'Company')
    ]
    userpic = models.ImageField(upload_to='userpics/', blank=True, null=True)
    role = models.CharField(max_length=3, choices=ROLES, default=USER)
    company = models.ForeignKey('self', limit_choices_to={'role': COMPANY}, blank=True, null=True)
    objects = UserManager()

    def __str__(self):
        return str(self.username)


class Event(models.Model):
    title = models.CharField(max_length=80)
    address = models.CharField(max_length=150)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()
    members = models.ManyToManyField(
        CustomUser,
        limit_choices_to={'role': CustomUser.USER},
        related_name='members_set',
        through="Participant",
        blank=True)
    sponsors = models.ManyToManyField(
        CustomUser,
        related_name='sponsors_set',
        limit_choices_to={'role': CustomUser.COMPANY},
        blank=True)

    def __str__(self):
        return str(self.title) + " " + str(self.start_time.year)


class Participant(models.Model):
    LISTENER = 'LS',
    SPEAKER = 'SP'
    ROLES = [
        ('LS', 'Listener'),
        ('SP', 'Speaker')
    ]
    user = models.ForeignKey(CustomUser)
    event = models.ForeignKey(Event)
    role = models.CharField(max_length=3, choices=ROLES, default=LISTENER)

    def __eq__(self, value):
        return self.value == value

    def __len__(self):
        return len(self.value)

    def __str__(self):
        return str(self.event) + " - " + str(self.user) + ' - ' + self.role


