"""
Definition of models.
"""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.



class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    number_of_guests = models.PositiveIntegerField()
    booking_datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.number_of_guests}"
    
class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)]
    )
   

    def __str__(self):
        return f"{self.title +str(self.price)}"

