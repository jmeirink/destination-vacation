from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('destinations/', views.destinations_index, name='destinations_index'),
  path('destinations/<int:destination_id>/', views.destinations_detail, name='destinations_detail'),
]