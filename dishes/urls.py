from django.urls import path

from . import views

app_name='dishes'


urlpatterns = [
    path('', views.index, name='index'),
    path('dishes/', views.leaderboard, name='leaderboard'),
    path('add-dish/', views.dishAdd, name='dishAdd'),
    path('dish_details/<int:dish_Id>', views.dish_details, name='dish_details'),
    path('hotel/add/', views.hotelAdd, name='hotelAdd'),  # Add this line
    # path('top-dishes-chart/', views.top_dishes_chart, name='top_dishes_chart'),
    path('graph/', views.dish_graph, name='dish_graph'),  # Add Graph URL

]