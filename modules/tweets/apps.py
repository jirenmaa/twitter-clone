from django.apps import AppConfig


class TweetsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "modules.tweets"

    def ready(self):
        from . import signals

        signals.trigger()

        return super().ready()
