from __future__ import unicode_literals

from django.apps import AppConfig


class ConfAppConfig(AppConfig):
    name = 'conf_app'

    def ready(self):
        import conf_app.signals