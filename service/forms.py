# -*- coding: utf-8 -*-
from django import forms


class NotificationForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        min_length=2,
        widget=forms.TextInput(attrs={"class":"form-control"}, ),
        label=u"Название"
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={"class":"form-control"}),
        label=u"Текст"
    )