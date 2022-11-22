# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect, reverse
from django.urls import reverse_lazy
# Create your views here.
from django.contrib.auth.models import  User
from .forms import NotificationForm
from .tasks import send_email_notification
from django.contrib import messages

def send_notify_emails(request):
    if request.method == "POST":
        form = NotificationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_email_notification.delay(data["title"], data["text"])
            messages.success(request, 'Рассылка успешно отправлена')
            return redirect(reverse_lazy("send_notify"))
    else:
        form = NotificationForm()
    context = {
        "form": form
    }
    return render(request, "index.html", context)