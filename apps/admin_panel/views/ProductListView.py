from apps.admin_panel.views.AdminRequiredMixin import AdminRequiredMixin
from apps.products.models.product import Product
from django.views.generic import ListView

class ProductListView(AdminRequiredMixin, ListView):
    template_name = 'admin_panel/products/list.html'
    model = Product
    context_object_name = 'products'
    
