from rest_framework import serializers
from .models import Book
from rest_framework.validators import UniqueValidator


# def validate_title(value):        
#         qs = Book.objects.filter(title__iexact=value)
#         if qs.exists():
#             raise serializers.ValidationError(f"{value} this title already exists")
#         return value

def validate_title(value):
    if "hello" in value.lower():
        raise serializers.ValidationError("Title cannot contain hello")
    return value

unique_title_validator = UniqueValidator(queryset=Book.objects.all(), message="this title already exists")