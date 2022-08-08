from django.db import models

# Create your models here.
class Destination(models.Model):
  destination = models.CharField(max_length=30)
  description = models.TextField(max_length=200)

  def __str__(self):
    return self.destination