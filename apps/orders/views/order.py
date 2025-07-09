from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from apps.orders.models import Order, OrderItem
from apps.cart.models import CartItem
from apps.addresses.models import Address
from apps.orders.serializers.order import OrderSerializer

class PlaceOrderView(APIView):
    def post(self, request):
        try:
            address = Address.objects.get(user=request.user)
        except Address.DoesNotExist:
            return Response({'detail': 'No address found'}, status=400)
        cart_items = CartItem.objects.filter(user=request.user)
        if not cart_items.exists():
            return Response({'detail': 'Cart is empty'}, status=400)
        order = Order.objects.create(user=request.user, address=address)
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
            )
            # Decrement stock:
            item.product.stock_quantity -= item.quantity
            item.product.save()
        cart_items.delete()
        return Response({'msg': 'Order placed'}, status=201)

class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)