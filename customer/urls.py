from django.urls import path
from . import views

urlpatterns = [
    path('dishes_details/', views.customer_dish_details, name='customer_dish_details'),
    #path('payment/', views.payment, name='payment'),
    #path('payment-success/', views.payment_success, name='payment_success'),  # Added payment success path
]
