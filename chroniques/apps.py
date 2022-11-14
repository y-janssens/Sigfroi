from django.apps import AppConfig


class ChroniquesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chroniques'

    def ready(self):
        import chroniques.signals  # noqa
