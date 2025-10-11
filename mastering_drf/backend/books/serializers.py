from rest_framework import serializers

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'ISBN',
            'price',
            'sale_price',
            'discount'
        ]
    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Book):
            return None
        return obj.get_discount()