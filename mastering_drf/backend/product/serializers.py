from rest_framework import serializers
from .models import Product, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            # "id",p
            "name",
            "description",
            "price",
            "stock"
        )

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name")
    product_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        source="product.price"
    )
    class Meta:
        model = OrderItem
        fields = (
            # 'pk',
            "product_name",
            "product_price",
            "quantity",
            "item_subtotal"
        )


class OrderCreateSerializer(serializers.ModelSerializer):
    class OrderItemCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = OrderItem
            fields = (
                'product',
                'quantity'
            )
    
    def create(self, validated_data):
        orderItem_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item in orderItem_data:
            OrderItem.objects.create(order=order, **item)

        return order
    
    order_id = serializers.UUIDField(read_only=True)
    items = OrderItemCreateSerializer(many=True)
    class Meta:
        model = Order
        fields = (
            'order_id',
            'user',
            'status',
            'items',
        )
        extra_kwargs = {
            'user': {'read_only': True}
        }
        

class OrderSerializer(serializers.ModelSerializer):
    order_id = serializers.UUIDField(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        order_items = obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)
    class Meta:
        model = Order
        fields = (
            "order_id",
            "user",
            "created_at",
            "status",
            "items",
            "total_price", 
        )

class ProductInfoSerializer(serializers.Serializer):
    Products = ProductSerializer(many=True)
    count = serializers.IntegerField()
    max_price = serializers.FloatField()