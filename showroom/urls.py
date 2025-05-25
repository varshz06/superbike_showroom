from django.urls import path
from . import views

urlpatterns = [
    path('', views.bike_list, name='bike_list'),           # Homepage -> bike list
    path('bikes/', views.bike_list, name='bike_list_alt'),  # Optional: alias for /bikes/
    path('add/', views.add_bike, name='add_bike'),          # Add new bike form
    path('bike/<int:bike_id>/', views.bike_detail, name='bike_detail'),  # Bike detail page
]
