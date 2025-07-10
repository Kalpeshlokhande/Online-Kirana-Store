from django.shortcuts import redirect, render
from django.views import View
from apps.orders.models.order import Order

class OrderListView(View):
    template_name = 'admin_panel/orders/list.html'

    def get(self, request):
        if not (request.user.is_authenticated and request.user.is_admin):
            return redirect('admin_login')
        
        orders = Order.objects.all().order_by('-created_at')
        return render(request, self.template_name, {'orders': orders})
    

