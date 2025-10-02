from django.db import models

# Create your models here.
class Tour(models.Model):
    # we need an origin country, destination, number of nights and price for that tour
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()
    
    # this is string representation of tours
    def __str__ (self):
        return (f"ID {self.id}, From {self.origin_country} To {self.destination_country}, Number_of_nights {self.number_of_nights}, price_per_night {self.price}")