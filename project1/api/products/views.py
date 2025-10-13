from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class CreateListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        if description is None:
            description = title
            serializer.save(description=description)
        serializer.save()

class RetrieveUpdateDestroyProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
