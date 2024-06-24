# email_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('verify-otp/<str:email>/', views.verify_otp, name='verify_otp'),
    path('success/', views.success, name='success'),
]
