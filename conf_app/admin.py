from django.contrib import admin

from .models import *

admin.site.register(Company)
admin.site.register(CustomUser)
admin.site.register(Event)
admin.site.register(Participant)
