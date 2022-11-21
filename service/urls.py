from django.conf.urls import url

from .views import send_notify_emails

urlpatterns = [
    url(r'', send_notify_emails, name="send_notify")
]