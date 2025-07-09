from django.urls import path
from apps.orders.views.order import PlaceOrderView, OrderListView

urlpatterns = [
    path('order/', PlaceOrderView.as_view()),
    path('orders/', OrderListView.as_view()),
]