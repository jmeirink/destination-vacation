from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Destination
from .forms import ActivityForm

# Views
class Home(LoginView):
  template_name = 'home.html'

@login_required # You can remove this if you dont want this functionality 
def destinations_index(request):
  destinations = Destination.objects.all() # Comment and uncomment next line to show just users destinations
  # destinations = Destination.objects.filter(user=request.user)
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

class DestinationCreate(LoginRequiredMixin, CreateView):
  model = Destination
  fields = ['destination', 'description']
  # success_url = '/destinations/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class DestinationUpdate(UpdateView):
  model = Destination
  fields = ['destination', 'description']

class DestinationDelete(DeleteView):
  model = Destination
  success_url = '/destinations/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('destinations_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)