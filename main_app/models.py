from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

TYPES = (
  ('A', 'Attractions'),
  ('S', 'Shopping'),
  ('D', 'Drinking & Dining')
)

# Create your models here.
class Destination(models.Model):
  destination = models.CharField(max_length=30)
  description = models.TextField(max_length=200)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.destination

  def get_absolute_url(self):
    return reverse('destinations_detail', kwargs={'destination_id': self.id})

class Activity(models.Model):
  activity = models.CharField(max_length=20)
  type = models.CharField(
    max_length=1,
    choices=TYPES,
    default=TYPES[0][0]
  )

  destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_type_display()} on {self.activity}"

  # class Meta:
  #   ordering = ['-date']