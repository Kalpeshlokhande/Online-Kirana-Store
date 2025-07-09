from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from apps.cart.models import CartItem
from apps.products.models import Product
from apps.cart.serializers.cart import CartItemSerializer

class AddToCartView(APIView):
    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        try:
            product = Product.objects.get(pk=product_id)
            cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity
            cart_item.save()
            return Response({"msg": "Added to cart"}, status=201)
        except Product.DoesNotExist:
            return Response({"detail": "Product not found"}, status=404)

class CartListView(APIView):
    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)