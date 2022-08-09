from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('destinations/', views.destinations_index, name='destinations_index'),
  path('destinations/<int:destination_id>/', views.destinations_detail, name='destinations_detail'),
  path('destinations/create/', views.DestinationCreate.as_view(), name='destinations_create'),
  path('destinations/<int:pk>/update/', views.DestinationUpdate.as_view(), name='destinations_update'),
  path('destinations/<int:pk>/delete/', views.DestinationDelete.as_view(), name='destinations_delete'),
  path('destinations/<int:destination_id>/add_activity/', views.add_activity, name='add_activity'),
  path('accounts/signup/', views.signup, name='signup'),
]