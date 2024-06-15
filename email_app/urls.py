# email_app/urls.py

from django.urls import path
from .views import home, verify_otp, success

urlpatterns = [
    path('', home, name='home'),
    path('verify-otp/<str:email>/', verify_otp, name='verify_otp'),
    path('success/', success, name='success'),
]
    


    # email_app/urls.py

# from django.urls import path
# from .views import home, success

# urlpatterns = [
#     path('', home, name='home'),
#     path('success/', success, name='success'),
# ]