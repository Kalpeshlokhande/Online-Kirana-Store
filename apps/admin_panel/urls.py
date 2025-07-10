from django.urls import path
from apps.admin_panel.views.AddProductView import  ProductAddView
from apps.admin_panel.views.AdminLoginView import AdminLoginView
from apps.admin_panel.views.AdminLogoutView import AdminLogoutView
from apps.admin_panel.views.EditProductView import ProductEditView
from apps.admin_panel.views.OrderDetailView import OrderDetailView
from apps.admin_panel.views.OrderListView import OrderListView
from apps.admin_panel.views.ProductListView import ProductListView 

app_name = 'apps.admin_panel'

urlpatterns = [
    path('login/', AdminLoginView.as_view(), name='login'),
    path('logout/', AdminLogoutView.as_view(), name='logout'),
    path('', ProductListView.as_view(), name='dashboard'),  
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/add/', ProductAddView.as_view(), name='product_add'),
    path('products/<int:pk>/edit/', ProductEditView.as_view(), name='product_edit'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
]