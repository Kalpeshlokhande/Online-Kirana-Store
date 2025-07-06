from django.urls import path, include
from .views import APIRootView

urlpatterns=[
    path('',APIRootView.as_view(),name='api-root'),
    path('users/',include('app.users.urls')),
    path('products/',include('app.users.products.urls')),
    path('cart/',include('app.cart.urls')),
    path('orders/',include('app.orders.urls')),
    
]

