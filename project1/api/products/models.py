from django.db import models
from django.contrib.auth.models import User 

class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE ,related_name="books")
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f'title: {self.title} owner: {self.owner}'

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.9)
    
    def get_discount(self):
        return "10%"