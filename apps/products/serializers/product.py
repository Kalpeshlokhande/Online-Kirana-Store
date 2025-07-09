from rest_framework import serializers
from apps.products.models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price', 'description', 'image', 'stock_quantity']