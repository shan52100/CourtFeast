from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.payment, name='payment'),
    path('payment-form/', views.payment_form, name='payment_form'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-success/', views.payment_success, name='payment_success'),  # Added payment success path
    path('payment-failure/', views.payment_failure, name='payment_failure'),  # Added payment success path
]
