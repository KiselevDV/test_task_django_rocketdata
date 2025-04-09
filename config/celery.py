import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

celery_app = Celery('config')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    'init_check_celery_beat_task': {
        'task': 'init.tasks.check_celery_beat_task',
        'schedule': crontab(minute='*'),
    },
    'increase_debt_every_3_hours': {
        'task': 'init.tasks.increase_debt',
        'schedule': crontab(minute=0, hour='*/3'),
    },
    'decrease_debt_daily_6_30': {
        'task': 'init.tasks.decrease_debt',
        'schedule': crontab(minute=30, hour=6),
    },
}
