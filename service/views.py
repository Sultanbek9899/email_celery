# -*- coding: utf-8 -*-
from django.shortcuts import render
# Create your views here.
from django.contrib.auth.models import  User
from .forms import NotificationForm
from .tasks import send_email_notification


def send_notify_emails(request):
    if request.method == "POST":
        form = NotificationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_email_notification(data["title"], data["text"])
    else:
        form = NotificationForm()
    context = {
        "form": form
    }
    return render(request, "index.html", context)