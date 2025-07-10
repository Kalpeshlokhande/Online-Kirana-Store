from django.shortcuts import redirect, render
from django.views import View
from apps.products.models.product import Product, Category
from django.contrib import messages

class EditProductView(View):
    template_name = 'admin_panel/products/edit.html'

    def get(self, request, product_id):
        if not (request.user.is_authenticated and request.user.is_admin):
            return redirect('admin_login')
        
        product = Product.objects.get(id=product_id)
        categories = Category.objects.all()
        return render(request, self.template_name, {
            'product': product,
            'categories': categories
        })

    def post(self, request, product_id):
        if not (request.user.is_authenticated and request.user.is_admin):
            return redirect('admin_login')
        
        try:
            product = Product.objects.get(id=product_id)
            product.name = request.POST.get('name')
            product.category_id = request.POST.get('category')
            product.price = request.POST.get('price')
            product.description = request.POST.get('description')
            product.stock_quantity = request.POST.get('stock_quantity')
            if 'image' in request.FILES:
                product.image = request.FILES['image']
            product.save()
            messages.success(request, 'Product updated successfully')
            return redirect('admin_products')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('admin_edit_product', product_id=product_id)
        
        