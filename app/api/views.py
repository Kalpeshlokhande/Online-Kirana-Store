from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,permissions,status
from django.contrib.auth.models import User
from app.users.models import UserProfile
from app.products.models import Category, Product
from app.cart.models import Cart,CartItem
from app.orders.models import Order,OrderItem
from .serializers import(
    RegisterSerializer, UserSerializer, UserProfileSerializer,
    CategorySerializer, ProductSerializer, CartItemSerializer, AddCartItemSerializer,
    OrderSerializer
)

# Create your views here.

class RegisterView(generics.CreateAPIView):
    serializer_class=RegisterSerializer

class ProfileView(generics.RetrieveAPIView):
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAuthenticated]
    def get_object(self):
        return self.request.user
    
class AddressUpdateView(generics.UpdateAPIView):
    serializer_class=UserProfileSerializer
    permission_classes=[permissions.IsAuthenticated]
    def get_object(self):
        return self.request.user.userprofile
    
class CategoryListView(generics.ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class ProductListView(generics.ListAPIView):
    serializer_class=ProductSerializer
    def get_queryset(self):
        category_id=self.request.query_params.get('category_id')
        if category_id:
            return Product.objects.filter(category_id=category_id)
        return Product.objects.all()

class AddToCartView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self,request):
        serializer=AddCartItemSerializer(data=request.data)
        if serializer.is_valid():
            product_id=serializer.validated_data['product_id']
            quantity = serializer.validated_data['quantity']
            product = Product.objects.get(id=product_id)
            cart,created=Cart.objects.get_or_create(user=request.user)
            cart_item,created=CartItem.objects.get_or_create(cart=cart,product=product)
            cart_item.quantity+=quantity
            cart_item.save()
            return Response({'message':'Product added to cart'})
        return Response(serializer.errors,status=400)
    
class ViewCart(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request):
        cart,created=Cart.objects.get_or_create(user=request.user)
        items=CartItem.objects.filter(cart=cart)
        serializer=CartItemSerializer(items,many=True)
        return Response(serializer.data)
    
class PlaceOrderView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        user = request.user
        address = user.userprofile.address
        if not address:
            return Response({'error': 'No address found.'}, status=400)
        cart = Cart.objects.get(user=user)
        items = CartItem.objects.filter(cart=cart)
        if not items:
            return Response({'error': 'Cart is empty.'}, status=400)
        order = Order.objects.create(user=user, address=address)
        for item in items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
            item.product.stock_quantity -= item.quantity
            item.product.save()
            item.delete()
        return Response({'message': 'Order placed successfully.'})

class OrdersListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)



