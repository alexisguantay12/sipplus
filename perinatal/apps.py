from django.apps import AppConfig


class PerinatalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'perinatal'

    def ready(self):
        import perinatal.signals
