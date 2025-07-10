from django.shortcuts import redirect, render
from django.views import View
from apps.products.models.category import Category
from apps.products.models.product import Product
from django.contrib import messages

class AddProductView(View):
    template_name = 'admin_panel/products/add.html'

    def get(self, request):
        if not (request.user.is_authenticated and request.user.is_admin):
            return redirect('admin_login')
        
        categories = Category.objects.all()
        return render(request, self.template_name, {'categories': categories})

    def post(self, request):
        if not (request.user.is_authenticated and request.user.is_admin):
            return redirect('admin_login')
        
        try:
            product = Product.objects.create(
                name=request.POST.get('name'),
                category_id=request.POST.get('category'),
                price=request.POST.get('price'),
                description=request.POST.get('description'),
                stock_quantity=request.POST.get('stock_quantity')
            )
            if 'image' in request.FILES:
                product.image = request.FILES['image']
                product.save()
            messages.success(request, 'Product added successfully')
            return redirect('admin_products')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('admin_add_product')

