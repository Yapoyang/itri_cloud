from django.db import models

# Create your models here.
class Restaurants(models.Model):
    name=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=15)
