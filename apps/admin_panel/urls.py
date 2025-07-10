from django.urls import path
from apps.admin_panel.views import AdminLoginView, AdminLogoutView, AdminDashboardView
from apps.admin_panel.views import ProductListView, AddProductView, EditProductView
from apps.admin_panel.views import OrderListView, OrderDetailView

urlpatterns = [
    path('login/', AdminLoginView.as_view(), name='admin_login'),
    path('logout/', AdminLogoutView.as_view(), name='admin_logout'),
    path('dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('products/', ProductListView.as_view(), name='admin_products'),
    path('products/add/', AddProductView.as_view(), name='admin_add_product'),
    path('products/edit/<int:product_id>/', EditProductView.as_view(), name='admin_edit_product'),
    path('orders/', OrderListView.as_view(), name='admin_orders'),
    path('orders/<int:order_id>/', OrderDetailView.as_view(), name='admin_order_detail'),
]