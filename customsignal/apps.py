from django.apps import AppConfig


class CustomsignalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customsignal'
    def ready(self):
        import customsignal.signals