from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Order, OrderItem
from .serializers import ProductSerializer, OrderSerializer
from django.shortcuts import get_object_or_404

@api_view(["GET"])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response({
        "data": serializer.data
    })

@api_view(["GET"])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response({
        "data": serializer.data
    })

@api_view(["GET"])
def order_list(request):
    orders = Order.objects.prefetch_related("items__product")
    serializer = OrderSerializer(orders, many=True)
    return Response({
        "data": serializer.data
    })