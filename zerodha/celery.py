from __future__ import absolute_import, unicode_literals

import os
from django.conf import settings

from celery import Celery

from celery.schedules import crontab

# if settings.LIVE:

print("Celery working!")

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zerodha.settings')
# if settings.LIVE:
app = Celery('zdh')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# -------------
#links
#(must) everything is available here https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html
# only helpful youtube video https://www.youtube.com/watch?v=yGGP0XNVe0w
# (must)amazing article on medium https://medium.com/@yedjoe/celery-4-periodic-task-in-django-9f6b5a8c21c7
#https://docs.celeryproject.org/en/latest/userguide/configuration.html#beat-scheduler
#https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html
# -------------
# Using custom scheduler classes( using django-celery-beat extension that stores the schedule in the Django database, and presents a convenient admin interface to manage periodic tasks at runtime.)
# There’s also the django-celery-beat extension that stores the schedule in the Django database, 
# and presents a convenient admin interface to manage periodic tasks at runtime.
# we can Visit the Django-Admin interface to set up some periodic tasks.
# https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#id8
#(1)
# CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler' in settings


# ORRRRRRRRRRRRR


# -------------
#(2)Default: "celery.beat:PersistentScheduler".

# app.conf.beat_schedule = {
#     "timepass-task": {
#         "task": "celery_app.tasks.long_process_2",
#         "schedule":crontab(hour=7, minute=30, day_of_week=1),
        
#     }
# }

# The default scheduler (storing the schedule in the celerybeat-schedule file) will automatically 
# detect that the time zone has changed, and so will reset the schedule itself, but other schedulers 
# may not be so smart (e.g., the Django database scheduler, see below) and in that case you’ll have to 
# reset the schedule manually.https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#id2

# The default scheduler is the celery.beat.PersistentScheduler, that simply keeps track of the last run
#  times in a local shelve database file.(it gets save at the location where our manage.py resides)

# There’s also the django-celery-beat extension that stores the schedule in the Django database, 
# and presents a convenient admin interface to manage periodic tasks at runtime.
# ----------

# Celery requires both of the worker and the beat in order for tasks to execute as planned.
# each of the worker and the beat service should be started separately by the following commands:
# Starting service manually is nice, but redundant. The solution is daemonization — making the services automatically starts along with the system.
# that what we do in production
# for more https://medium.com/@yedjoe/celery-4-periodic-task-in-django-9f6b5a8c21c7

# -------

# amazing 3 medium articles, 3 parts

# part 1: https://medium.com/the-andela-way/asynchronous-processing-in-celery-79f88fa599a5
# part 2: https://medium.com/the-andela-way/timed-periodic-tasks-in-celery-58c99ecf3f80
# part 3: https://medium.com/the-andela-way/crontabs-in-celery-d779a8eb4cf

# -------
#https://pawelzny.com/python/celery/2017/08/14/celery-4-tasks-best-practices/
# ------
# read about this more in future apply_async
# https://stackoverflow.com/questions/57269053/how-to-start-a-task-at-a-specific-time-with-django-celery
# ------
# getting started with celery
# https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
# https://docs.celeryproject.org/en/stable/userguide/calling.html#guide-calling
# https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html#choosing-a-broker
# prodcution tips https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html#running-the-celery-worker-server
# -----------
#helped at beginning..
#https://www.youtube.com/watch?v=b-6mEAr1m-A
#------------
# NOTE
# while changing code in background tasks in prodcution...wee need to deploy our chanegs first 
# then we need to restart both worker and beat service...thats those 2 commands we need to re run
# ----------------------------
# requirements
# celery==4.4.2
# Django==2.0 (getting error in windows while starting  worker...so used old version)
# django-celery-beat==2.0.0
# redis
# eventlet==0.25.2(getting error for windows so used this while starting worker from cmd)
# ----------------
# for production
# https://realpython.com/asynchronous-tasks-with-django-and-celery/
# https://medium.com/@yedjoe/celery-4-periodic-task-in-django-9f6b5a8c21c7
# --------------