from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from dishes.models import Hotel,dishes
#import razorpay
import json

# Razorpay client initialization
#client = razorpay.Client(auth=("YOUR_KEY_ID", "YOUR_KEY_SECRET"))

def customer_dish_details(request):
    hotels = Hotel.objects.all()
    hotel_dishes = {}
    for hotel in hotels:
        hotel_dishes[hotel] = dishes.objects.filter(hotel=hotel)
    return render(request, 'dish_detail.html', {'hotel_dishes': hotel_dishes})

