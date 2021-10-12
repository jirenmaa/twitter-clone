from django.apps import AppConfig


class TweetsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "modules.v1.tweets"

    def ready(self) -> None:
        from . import signals
        signals.trigger()

        return super().ready()
