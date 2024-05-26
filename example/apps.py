from django.apps import AppConfig
import os


class ExampleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'example'
    def ready(self):
        from django.core.management import call_command
        if os.environ.get('RUN_MAIN', None) != 'true':  # Prevent from running twice with autoreload
            call_command('runserver_bot')