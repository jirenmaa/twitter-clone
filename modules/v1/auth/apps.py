from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "modules.v1.auth"
    # use label attribute to create unique name for the app
    # because django already use the auth app as the built-in app
    # https://docs.djangoproject.com/en/3.2/ref/applications/#django.apps.AppConfig.label
    label = "v1_auth"
