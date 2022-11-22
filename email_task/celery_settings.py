from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_task.settings')
app = Celery('email_task')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
