from django.apps import AppConfig
from django.core.management import call_command


class ProviderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'service'

    def ready(self):
        call_command("makemigrations")
        call_command("migrate")
        call_command("load_csv")