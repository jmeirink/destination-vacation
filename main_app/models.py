from django.db import models
from django.urls import reverse

# Create your models here.
class Destination(models.Model):
  destination = models.CharField(max_length=30)
  description = models.TextField(max_length=200)

  def __str__(self):
    return self.destination

  def get_absolute_url(self):
    return reverse('destinations_detail', kwargs={'destination_id': self.id})