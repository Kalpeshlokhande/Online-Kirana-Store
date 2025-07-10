from django.views.generic import UpdateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from apps.admin_panel.forms.ProductForm import ProductForm
from apps.admin_panel.views.AdminRequiredMixin import AdminRequiredMixin
from apps.products.models import Product, Category

class ProductEditView(AdminRequiredMixin, UpdateView):
    template_name = 'admin_panel/products/edit.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('admin_panel:product_list')