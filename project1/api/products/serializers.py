from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'owner',
            'id',
            'title',
            'description',
            'price',
            'sale_price',
            'get_discount'
        ]


    