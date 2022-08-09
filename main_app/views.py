from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Destination
from .forms import ActivityForm
from django.views.generic import ListView

# Views
def home(request):
  return render(request, 'home.html')

def destinations_index(request):
  destinations = Destination.objects.all()
  return render(request, 'destinations/index.html', { 'destinations': destinations })

def destinations_detail(request, destination_id):
  destination = Destination.objects.get(id=destination_id)
  activity_form = ActivityForm()
  return render(request, 'destinations/detail.html', { 'destination': destination, 'activity_form': activity_form })

def add_activity(request, destination_id):
  form = ActivityForm(request.POST)
  if form.is_valid():
    new_activity = form.save(commit=False)
    new_activity.destination_id = destination_id
    new_activity.save()
  return redirect('destinations_detail', destination_id=destination_id)

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