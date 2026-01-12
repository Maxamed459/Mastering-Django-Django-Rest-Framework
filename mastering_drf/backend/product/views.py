from django.db.models import Max
from django.shortcuts import get_object_or_404, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action

from api.filters import ProductFilter, inStockFilterBackend, OrderFilter

from .models import Order, OrderItem, Product
from .serializers import (OrderSerializer, ProductInfoSerializer,
                          ProductSerializer, OrderCreateSerializer)


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
        inStockFilterBackend
    ]
    search_fields = ['=name', 'description']
    ordering_fields = ['name', 'price', 'stock']


    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class RetrieveProductAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = "product_id"

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class orderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related("items__product")
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)
        return qs

# class OrderListAPIView(generics.ListAPIView):
#     queryset = Order.objects.prefetch_related("items__product")
#     serializer_class = OrderSerializer

class UserOrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related("items__product")
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    # only returns the current user orders only
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

class ProductInfoAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductInfoSerializer({
            "Products": products,
            "count": len(products),
            "max_price": products.aggregate(max_price=Max("price"))["max_price"]
        })
        return Response(serializer.data)
        