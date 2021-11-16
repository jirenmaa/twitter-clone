import os
from datetime import timedelta
from pathlib import Path

import dotenv

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

# read environment variables from .env
dotenv.read_dotenv(dotenv=os.path.join(BASE_DIR, ".envs/django/.django"))
dotenv.read_dotenv(dotenv=os.path.join(BASE_DIR, ".envs/postgres/.postgres"))

WEBSITE_URL = os.getenv("WEBSITE_URL")

DATABASE_HOST = os.getenv("POSTGRES_DOCKER_HOST")
DATABASE_HOST = DATABASE_HOST if DATABASE_HOST else os.getenv("POSTGRES_HOST")

DJANGO_DEFAULT_URL = os.getenv("DJANGO_DEFAULT_URL", "localhost:8000/")
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = os.getenv("DEBUG")
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "UTC"
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1", "localhost"]
# https://docs.djangoproject.com/en/3.2/ref/settings/#migration-modules
MIGRATION_MODULES = {
    "tweets": "database.migrations.tweets",
    "users": "database.migrations.users",
    "actions": "database.migrations.actions",
}
# https://docs.djangoproject.com/en/3.2/ref/settings/#conn-max-age
CONN_MAX_AGE = 60 * 5


# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "configs.urls"
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "configs.server.wsgi.application"


# CORS HEADERS
# ------------------------------------------------------------------------------
# https://pypi.org/project/django-cors-headers/#cors-allowed-origins
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
]


# APPS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/ref/applications/#module-django.apps
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]
THIRD_PARTY_APPS = [
    "corsheaders",
    "cloudinary",
    "cloudinary_storage",
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",
]
LOCAL_APPS = [
    "modules.auth.apps.AuthenticationConfig",
    "modules.users.apps.UsersConfig",
    "modules.tweets.apps.TweetsConfig",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": os.getenv("POSTGRES_ENGINE"),
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": DATABASE_HOST,
        "PORT": os.getenv("POSTGRES_PORT"),
    },
    "replica": {
        "ENGINE": os.getenv("REPLICA_ENGINE"),
        "NAME": os.getenv("REPLICA_NAME"),
        "USER": os.getenv("REPLICA_USER"),
        "PASSWORD": os.getenv("REPLICA_PASSWORD"),
        "HOST": DATABASE_HOST,
        "PORT": os.getenv("REPLICA_PORT"),
        "TEST": {
            "MIRROR": "default",
        },
        "SUPPORTS_TRANSACTIONS": True,
    },
}


# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "account_login"


# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        "DIRS": [
            os.path.join(BASE_DIR, "modules", "templates"),
            os.path.join(BASE_DIR, "celeryapp", "workers", "templates"),
        ],
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]


# MEDIA STORAGE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/howto/static-files/#configuring-static-files
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/3.2/howto/static-files/#serving-files-uploaded-by-a-user-during-development
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
# https://docs.djangoproject.com/en/3.2/ref/files/storage/#module-django.core.files.storage
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
# https://pypi.org/project/django-cloudinary-storage/
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("CLOUD_NAME"),
    "API_KEY": os.getenv("API_KEY"),
    "API_SECRET": os.getenv("API_SECRET"),
}


# Email
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/topics/email/#smtp-backend
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5
# https://docs.djangoproject.com/en/3.2/ref/settings/#email-host
EMAIL_HOST = "smtp.gmail.com"
# https://docs.djangoproject.com/en/3.2/ref/settings/#email-host-user
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
# https://docs.djangoproject.com/en/3.2/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
# https://docs.djangoproject.com/en/3.2/ref/settings/#email-port
EMAIL_PORT = 587
# https://docs.djangoproject.com/en/3.2/ref/settings/#email-use-tls
EMAIL_USE_TLS = True
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = "twitter-clone <noreply@twitter-clone.com>"


# JWT
# ------------------------------------------------------------------------------
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html#settings
SIMPLE_JWT = {
    # You have the option of changing the token lifetime to anything you want.
    # (days, hours, minutes, seconds)
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=2),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer", "JWT"),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(hours=1),
}


# Celery
# ------------------------------------------------------------------------------
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#broker-transport
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://127.0.0.1:6379/0")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://127.0.0.1:6379/0")
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = os.getenv("CELERY_TIMEZONE", "Asia/Bangkok")
CELERY_ENABLE_UTC = True
CELERY_RESULT_EXPIRES = timedelta(seconds=10)

# REDIS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/ref/settings/#redis-host
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
# https://docs.djangoproject.com/en/3.2/ref/settings/#redis-port
REDIS_PORT = os.getenv("REDIS_PORT", 6379)
# https://docs.djangoproject.com/en/3.2/ref/settings/#redis-db
REDIS_DB = os.getenv("REDIS_DB", 0)
