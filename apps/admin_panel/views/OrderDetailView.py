from django.views.generic import DetailView
from apps.admin_panel.views.AdminRequiredMixin import AdminRequiredMixin
from apps.orders.models.order import Order


class OrderDetailView(AdminRequiredMixin, DetailView):
    model = Order
    template_name = 'admin_panel/orders/detail.html'
    context_object_name = 'order'
        
            
