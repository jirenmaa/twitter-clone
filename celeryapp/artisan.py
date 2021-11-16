from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

# set the default Django settings module for the 'celery' program
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "configs.settings.locals")

# initailize Celery
app = Celery("src")

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(packages=['celeryapp.tasks'])
