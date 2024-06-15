# email_app/utils.py

import random
from django.core.mail import send_mail
from django.conf import settings

def generate_otp():
    return random.randint(100000, 999999)

def send_email_to_client(subject, message, recipient_list):
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, recipient_list)



# email_app/utils.py

# from django.core.mail import send_mail
# from django.conf import settings

# def send_email_to_client(subject, message, recipient_list):
#     from_email = settings.EMAIL_HOST_USER
#     send_mail(subject, message, from_email, recipient_list)