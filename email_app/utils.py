# email_app/utils.py

# email_app/utils.py

import random
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

def generate_otp():
    return random.randint(100000, 999999)

def send_email_to_client(subject, message, recipient_list, attachment_path=None):
    from_email = settings.EMAIL_HOST_USER

    email_message = EmailMessage(subject, message, from_email, recipient_list)
    email_message.content_subtype = 'html'  # If your message contains HTML content

    if attachment_path:
        email_message.attach_file(attachment_path)
    
    email_message.send()


# email_app/utils.py

# from django.core.mail import send_mail
# from django.conf import settings

# def send_email_to_client(subject, message, recipient_list):
#     from_email = settings.EMAIL_HOST_USER
#     send_mail(subject, message, from_email, recipient_list)
