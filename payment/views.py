from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
#from dishes.models import Hotel, dish
#import razorpay
import json

# Razorpay client initializa
# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse

def payment_form(request):
    amount = request.GET.get('amount', 0)
    return render(request, 'paymentnew.html', {'amount': amount})

def payment(request):
    return render(request, 'payment.html')

def process_payment(request):
    if request.method == 'POST':
    
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')
        amount = request.POST.get('amount')

        import random
        payment_success = True  
        
        if payment_success:
            return redirect('payment_success')  # Pass amount as a URL parameter
        else:
            return redirect('payment_failure')

    return HttpResponse("Invalid request", status=400)

def payment_success(request):
    return render(request, 'success.html')

def payment_failure(request):
    return render(request, 'failure.html')
