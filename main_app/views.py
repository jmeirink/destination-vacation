from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Destination
from django.views.generic import ListView

# Views
def home(request):
  return render(request, 'home.html')

def destinations_index(request):
  destinations = Destination.objects.all()
  return render(request, 'destinations/index.html', { 'destinations': destinations })

def destinations_detail(request, destination_id):
  destination = Destination.objects.get(id=destination_id)
  return render(request, 'destinations/detail.html', { 'destination': destination })

class DestinationCreate(CreateView):
  model = Destination
  fields = '__all__'
  success_url = '/destinations/'

class DestinationUpdate(UpdateView):
  model = Destination
  fields = ['destination', 'description']

class DestinationDelete(DeleteView):
  model = Destination
  success_url = '/destinations/'