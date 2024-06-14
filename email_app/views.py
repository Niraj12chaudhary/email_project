# email_app/views.py

from django.shortcuts import render, redirect
from .utils import send_email_to_client

def home(request):
    
    subject = "This email is from Django server sent by shivam"
    message = "This is just a test message from Django server email"
    recipient_list = ["shivamkr7822@gmail.com"]  # Replace with the recipient's email

    send_email_to_client(subject, message, recipient_list)
    return redirect('success')
    
    return render(request, 'home.html')

def success(request):
    return render(request, 'success.html')

