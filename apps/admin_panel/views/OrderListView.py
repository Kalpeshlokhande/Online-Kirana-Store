from apps.admin_panel.views.AdminRequiredMixin import AdminRequiredMixin
from apps.orders.models.order import Order
from django.views.generic import ListView

class OrderListView(AdminRequiredMixin, ListView):
    model = Order
    template_name = 'admin_panel/orders/list.html'
    context_object_name = 'orders'
    queryset = Order.objects.select_related('user', 'address').order_by('-created_at')
    

