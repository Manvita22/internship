from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Location
from .forms import LocationForm
from django.contrib.auth.decorators import login_required
@login_required
def home(request):
    locations = Location.objects.filter(user=request.user)
    return render(request, 'locations/home.html', {'locations': locations})

def add_location(request):
    form = LocationForm(data=request.POST or None, files=request.FILES or None)
    if request.method == "POST" and form.is_valid():
        location = form.save(commit=False)
        location.user = request.user
        location.save()
        messages.success(request, "Location added successfully.")
        return redirect('home')
    return render(request, 'locations/add_location.html', {'form': form})

def location_view(request):
    locations = Location.objects.filter(user=request.user)
    return render(request, 'locations/locationview.html', {'locations': locations})

