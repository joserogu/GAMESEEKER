from django.apps import AppConfig


class WagGameseekConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wag_gameseek'

    def ready(self):
        import wag_gameseek.signals
