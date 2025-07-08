from django.urls import path
from .views import (
    AdminLoginView, AdminLogoutView, DashboardView,
    AddItemView, UpdateItemView, ViewOrdersView
)

urlpatterns = [
    path('login/', AdminLoginView.as_view(), name='admin_login'),
    path('logout/', AdminLogoutView.as_view(), name='admin_logout'),
    path('dashboard/', DashboardView.as_view(), name='admin_dashboard'),
    path('add-item/', AddItemView.as_view(), name='add_item'),
    path('update-item/<int:pk>/', UpdateItemView.as_view(), name='update_item'),
    path('orders/', ViewOrdersView.as_view(), name='view_orders'),
]