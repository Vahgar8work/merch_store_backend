from rest_framework import serializers
from .models import Order, OrderItem
from discounts.models import DiscountCode

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'printing_name', 'size', 'image_url']

class DiscountCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCode
        fields = ['code', 'discount_percentage', 'max_uses', 'expiry_date', 'custom']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    created_at = serializers.SerializerMethodField()
    is_verified = serializers.SerializerMethodField()
    discount_code = DiscountCodeSerializer(read_only=True)
    total_amount = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        return obj.created_at.isoformat()
    
    def get_is_verified(self, obj):
        if obj.is_verified is None:
            return "Pending"
        if obj.is_verified:
            return "Verified"
        return "Not Verified"
    
    def get_total_amount(self, obj):
        return obj.total_amount

    class Meta:
        model = Order
        fields = ['id', 'amount', 'created_at', 'is_verified', 'order_items', 'discount_code', 'total_amount']
