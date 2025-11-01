from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User


class BookQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)
    
    def search(self, query, user=None):
        lookup = Q(title__icontains=query)
        qs = self.published().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs

class ProductManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return BookQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)


class Book(models.Model):
    user = models.ForeignKey(User, default=1, null=True,  on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    published = models.BooleanField(default=True)

    objects = ProductManager()

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.ISBN}, Price: {self.price})"

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)
    
    def get_discount(self):
        return "20%"


    # def __str__(self):
    #     return f"Book Title {self.title} and book author is {self.author} also the ISBN is {self.ISBN} and the price is {self.price}"
