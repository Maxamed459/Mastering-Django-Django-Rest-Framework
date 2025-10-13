from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.title

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.9)
    
    def get_discount(self):
        return "10%"