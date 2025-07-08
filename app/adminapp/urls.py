from django.urls import path
from .views import (
    AdminRegisterView, AdminLoginView, AdminLogoutView,
    AdminDashboardView, AddItemView, UpdateItemView, ViewOrdersView
)

app_name = 'adminapp'

urlpatterns = [
    path('register/', AdminRegisterView.as_view(), name='register'),
    path('login/', AdminLoginView.as_view(), name='login'),
    path('logout/', AdminLogoutView.as_view(), name='logout'),
    path('dashboard/', AdminDashboardView.as_view(), name='dashboard'),
    path('add-item/', AddItemView.as_view(), name='add-item'),
    path('update-item/<int:pk>/', UpdateItemView.as_view(), name='update-item'),
    path('view-orders/', ViewOrdersView.as_view(), name='view-orders'),
]