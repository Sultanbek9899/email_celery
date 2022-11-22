from email_task.celery_settings import app
from django.contrib.auth.models import User
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings

from .utils import get_email_string,get_messages


@app.task
def send_email_notification(title, text):
    messages = get_messages(title, text)
    send_mass_mail(messages, fail_silently=False)
