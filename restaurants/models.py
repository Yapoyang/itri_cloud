from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Restaurant(models.Model):
   name=models.CharField(max_length=20)
   phone_number=models.CharField(max_length=20)
   address=models.CharField(max_length=50, blank=True)

   def __str__(self):
        return self.name

class Food(models.Model):
   name=models.CharField(max_length=20)
   price=models.DecimalField(max_digits=3,decimal_places=0)
   comment=models.CharField(max_length=50, blank=True)
   is_spicy=models.BooleanField(default=False)
   restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
   
   def __str__(self):
        return self.name

class Comment(models.Model):
   content=models.CharField(max_length=255)
   visitor=models.CharField(max_length=255)
   email=models.EmailField(max_length=255)
   date_time=models.DateTimeField()
   restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
   class Meta:
       ordering=['date_time']
       permissions=(("can_comment","Can comment"),)
