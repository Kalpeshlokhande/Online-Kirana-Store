from rest_framework import generics, permissions
from apps.products.models import Product
from apps.products.serializers.product import ProductSerializer

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        qs = Product.objects.all()
        if category_id:
            qs = qs.filter(category_id=category_id)
        return qs