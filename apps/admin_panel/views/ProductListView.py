from django.shortcuts import redirect, render
from django.views import View
from apps.products.models.product import Product

class ProductListView(View):
    template_name = 'admin_panel/products/list.html'

    def get(self, request):
        if not (request.user.is_authenticated and request.user.is_admin):
            return redirect('admin_login')
        
        products = Product.objects.all()
        return render(request,self.template_name,{'products':products})
    

