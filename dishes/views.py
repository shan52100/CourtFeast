from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date, timedelta
from django.http import HttpResponse

from .models import dishes, dish_votes
from users.models import user_votes
from foodcourt.settings import BASE_DIR
import matplotlib.pyplot as plt  # Ensure this is imported
from io import BytesIO
import base64
# Create your views here.
def index(request):
    return render(request, 'index.html')

def leaderboard(request):
    today = date.today()
    top_dishes = dish_votes.objects.filter(v_Date=today).order_by('-d_Votes').values()
    all_dishes = dishes.objects.all()
    return render(request, 'leaderboard2.html', {
        'dish': all_dishes,
        'top_dishes': top_dishes,
        'BASE_DIR': BASE_DIR
    })


@login_required(login_url='/login')
def dish_details(request, dish_Id):
    dish = dishes.objects.get(dish_Id=dish_Id)
    hotel_name = dish.hotel.h_Name  # Get hotel name from the related hotel object
    user_email = request.user.email

    # Determine if voting is enabled
    enable = True
    today_votes = user_votes.objects.filter(user_Id=user_email, v_Date=date.today(), dish_Id=dish_Id)
    if today_votes.exists():
        enable = False

    if request.method == 'POST' and enable:
        # Save user's vote
        user_vote = user_votes(user_Id=user_email, dish_Id=dish.dish_Id, dish_Name=dish.d_Name)
        user_vote.save()

        # Increment dish's vote count
        dish_vote, created = dish_votes.objects.get_or_create(
            dish_Id=dish.dish_Id,
            defaults={
                'd_Name': dish.d_Name,
                'd_Description': dish.d_Description,
                'd_Ingredients': dish.d_Ingredients,
                'd_Type': dish.d_Type,
                'd_Price': dish.d_Price,
                'd_Photo': dish.d_Photo,
                'v_Date': date.today(),
                'd_Votes': 1
            }
        )
        if not created:
            dish_vote.d_Votes += 1
            dish_vote.save()

        messages.success(request, "We Counted Your Vote!")
        return redirect('dishes:dish_details', dish_Id)

    return render(request, 'menu2.html', {
        'dish': dish,
        'hotel_name': hotel_name,  # Pass hotel name to the template
        'user_email': user_email,
        'enable': enable,
        'BASE_DIR': BASE_DIR
    })
from django.shortcuts import render, redirect
from django.contrib import messages



from .models import dishes, Hotel  # Import Hotel model

def dishAdd(request):
    hotels = Hotel.objects.all()  # Fetch all hotels to display in the form
    
    if request.method == 'POST':
        selected_hotel_id = request.POST.get("hotel")  # Get selected hotel ID
        selected_hotel = Hotel.objects.get(hotel_Id=selected_hotel_id)  # Retrieve hotel instance
        
        dish_data = dishes(
            d_Name=request.POST.get("dName"),
            d_Description=request.POST.get("dDescription"),
            d_Ingredients=request.POST.get("dIngredients"),
            d_Price=request.POST.get("dPrice"),
            d_Type=request.POST.get("dtype"),
            d_Photo=request.FILES.get("dPhoto"),
            hotel=selected_hotel  # Associate dish with selected hotel
        )
        dish_data.save()
        messages.success(request, "Your Dish Added Successfully")
        return redirect('dishes:leaderboard')  # Redirect to leaderboard

    return render(request, 'dish_add.html', {'hotels': hotels})

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Hotel

def hotelAdd(request):
    if request.method == 'POST':
        h_Name = request.POST.get("hName")
        h_Address = request.POST.get("hAddress")
        h_Contact = request.POST.get("hContact")

        # Save the new hotel instance
        hotel = Hotel(h_Name=h_Name, h_Address=h_Address, h_Contact=h_Contact)
        hotel.save()

        messages.success(request, "Hotel added successfully!")
        return redirect('/add-dish')  # Redirect to the same page or elsewhere as desired

    return render(request, 'hotel_add.html')


def dish_graph(request):
    # Fetch data for all dishes (no date filter applied)
    all_dishes = dishes.objects.all().order_by('-d_Price')

    # Check if there is any data
    if not all_dishes.exists():
        return render(request, 'dish_graph.html', {'graph_image': None, 'message': 'No dishes found.'})

    # Prepare data for the graph
    dish_names = [dish.d_Name for dish in all_dishes]
    dish_prices = [dish.d_Price for dish in all_dishes]

    # Create a Bar Chart
    plt.figure(figsize=(10, 6))
    bars = plt.bar(dish_names, dish_prices, color='skyblue')

    # Add labels and title
    plt.xlabel('Dishes')
    plt.ylabel('Price')
    plt.title('Dish Prices')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha="right")

    # Adjust layout to make space for rotated labels
    plt.tight_layout()

    # Convert the plot to a PNG image in memory
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graph_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    return render(request, 'dish_graph.html', {'graph_image': graph_image})