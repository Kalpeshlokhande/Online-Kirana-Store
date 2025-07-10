from django.urls import reverse_lazy
from apps.admin_panel.forms.ProductForm import ProductForm
from django.views.generic import CreateView
from apps.admin_panel.views.AdminRequiredMixin import AdminRequiredMixin


class ProductAddView(AdminRequiredMixin, CreateView):
    template_name = 'admin_panel/products/add.html'
    form_class = ProductForm
    success_url = reverse_lazy('admin_panel:product_list')