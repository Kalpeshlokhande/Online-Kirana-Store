from django.urls import path
from apps.cart.views.cart import AddToCartView, CartListView

urlpatterns = [
    path('cart/add/', AddToCartView.as_view()),
    path('cart/', CartListView.as_view()),
]