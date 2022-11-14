from django.apps import AppConfig


class FichesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fiches'

    def ready(self):
        import fiches.signals  # noqa
