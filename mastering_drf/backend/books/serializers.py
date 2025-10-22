from rest_framework import serializers
from rest_framework.reverse import reverse
from . import validators

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    title  = serializers.CharField(validators=[
        validators.unique_title_validator,
        validators.validate_title
    ])
    class Meta:
        model = Book
        fields = [
            'url',
            'id',
            'title',
            'author',
            'ISBN',
            'price',
            'sale_price',
            'discount'
        ]


    # def validate_title(self, value):
    #     qs = Book.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} this title already exists")
    #     return value

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("book-detail", kwargs={"pk": obj.pk}, request=request)

    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Book):
            return None
        return obj.get_discount()