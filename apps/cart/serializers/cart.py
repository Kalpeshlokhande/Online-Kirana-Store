from rest_framework import serializers
from apps.cart.models import CartItem
from apps.products.serializers.product import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']