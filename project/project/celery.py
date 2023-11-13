from __future__ import absolute_import, unicode_literals

import os
from datetime import timedelta
from time import sleep

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "project.settings")

app = Celery('project')

# update timezone
# app.conf.enable_utc = False
# app.conf.update(timezone='Asia/Dhaka')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(name="addition_task")
def add(x: int, y: int):
    sleep(20)
    return x + y


# Method 2
# Celery Beat Settings
# app.conf.beat_schedule = {
#     'every-1-minutes': {
#         'task': 'core.tasks.clear_session_cache',
#         'schedule': 10,
#         'args': ('11111',)
#     }
#     # Add more periodic tasks as needed
# }


# Using timedelta
# app.conf.beat_schedule = {
#     'every-01-minute': {
#         'task': 'core.tasks.clear_session_cache',
#         'schedule': timedelta(seconds=10),
#         'args': ('777',)
#     }
#     # Add more periodic tasks as needed
# }


# app.conf.beat_schedule = {
#     'every-10-seconds': {
#         'task': 'core.tasks.clear_session_cache',
#         'schedule': crontab(minute='*/1'),
#         'args': ('11111',)
#     }
#     # Add more periodic tasks as needed
# }

# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
