from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField()
    # Add other fields as necessary


# Create your models here.
