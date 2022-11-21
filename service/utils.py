from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf.global_settings import EMAIL_HOST_USER


def get_email_string(user, text):
    if isinstance(user, User):
        template_name = "email_template.html"
        data = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "text": text,
        }
        email = render_to_string(template_name, data)
        return email
    else:
        # Need logging
        print("TypeError. Check data")


def get_messages(title, text):
    messages = []
    users = User.objects.filter(is_active=True)
    for user in users:
        email_text = get_email_string(user, text)
        m = (title, email_text, EMAIL_HOST_USER, [user.email])
        messages.append(m)
    return messages
