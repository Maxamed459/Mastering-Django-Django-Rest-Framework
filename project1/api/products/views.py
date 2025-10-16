from rest_framework import generics, authentication, permissions
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsOwnerOrReadOnlyOnly

class CreateListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnlyOnly]

    def perform_create(self, serializer):
        owner = self.request.user
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        if description is None:
            description = title
            serializer.save(description=description, owner=owner)
        serializer.save()

class RetrieveUpdateDestroyProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnlyOnly]
    lookup_field = 'pk'
