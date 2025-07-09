from rest_framework import generics, permissions
from apps.products.models import Category
from apps.products.serializers.category import CategorySerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]