from django.shortcuts import render, get_object_or_404
from .models import Bike

def home(request):
    return render(request, 'showroom/home.html')

def bike_list(request):
    bikes = Bike.objects.all()
    return render(request, 'showroom/bike_list.html', {'bikes': bikes})

def bike_detail(request, bike_id):
    bike = get_object_or_404(Bike, pk=bike_id)
    return render(request, 'showroom/bike_detail.html', {'bike': bike})

from .forms import BikeForm
from django.shortcuts import redirect

def add_bike(request):
    if request.method == 'POST':
        form = BikeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bike_list')
    else:
        form = BikeForm()
    return render(request, 'showroom/add_bike.html', {'form': form})
