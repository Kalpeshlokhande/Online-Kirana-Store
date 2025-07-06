from django.urls import path
from .views import (
    RegisterView, ProfileView, AddressUpdateView,
    CategoryListView, ProductListView,
    AddToCartView, ViewCart,
    PlaceOrderView, OrdersListView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/address/', AddressUpdateView.as_view(), name='address-update'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/', ViewCart.as_view(), name='view-cart'),
    path('order/', PlaceOrderView.as_view(), name='place-order'),
    path('orders/', OrdersListView.as_view(), name='order-list'),
]