from django.shortcuts import redirect, render
from django.views import View
from apps.orders.models.order import Order

class OrderDetailView(View):
    template_name = 'admin_panel/orders/detail.html'

    def get(self, request, order_id):
        if not (request.user.is_authenticated and request.user.is_admin):
            return redirect('admin_login')
        
        order = Order.objects.get(id=order_id)
        return render(request, self.template_name, {'order': order})
        
            
