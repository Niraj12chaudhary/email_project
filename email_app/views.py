

# email_app/views.py for send email 

# from django.shortcuts import render, redirect
# from .utils import send_email_to_client

# def home(request):
    
#     subject = "This email is from Django server sent by shivam"
#     message = "This is just a test message from Django server email"
#     recipient_list = ["shivamkr7822@gmail.com"]  # Replace with the recipient's email

#     send_email_to_client(subject, message, recipient_list)
#     return redirect('success')
    
#     return render(request, 'home.html')

# def success(request):
#     return render(request, 'success.html')































# email_app/views.py
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.core.cache import cache
from .utils import generate_otp, send_email_to_client

def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get email from the form
        otp = generate_otp()  # Generate a 6-digit OTP
        cache.set(email, otp, timeout=300)  # Store OTP in cache for 5 minutes
        
        subject = "Your OTP Code"
        message = f"Your OTP code is {otp}"
        recipient_list = [email]  # Send OTP to the email address entered by the user
        
        send_email_to_client(subject, message, recipient_list)  # Send email
        return redirect('verify_otp', email=email)  # Redirect to OTP verification page
    
    return render(request, 'home.html')  # Render the form to enter email

def verify_otp(request, email):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        stored_otp = cache.get(email)
        
        if entered_otp == str(stored_otp):
            return redirect('success')
        else:
            return render(request, 'verify_otp.html', {'error': 'Invalid OTP', 'email': email})
    
    return render(request, 'verify_otp.html', {'email': email})

def success(request):
    return render(request, 'success.html')
