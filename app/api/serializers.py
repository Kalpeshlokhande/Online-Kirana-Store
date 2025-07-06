from rest_framework import serializers
from django.contrib.auth.models import User
from app.users.models import UserProfile
from app.products.models import Category, Product
from app.cart.models import CartItem
from app.orders.models import Order, OrderItem

class RegisterSerializer(serializers.ModelSerializer):
    phone = serializers.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        phone = validated_data.pop('phone')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, phone=phone)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address']

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(source='userprofile', read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price', 'description', 'image', 'stock_quantity']

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']

class AddCartItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id', 'address', 'status', 'created_at', 'items']