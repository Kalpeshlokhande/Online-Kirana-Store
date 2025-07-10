from django.shortcuts import redirect, render
from django.views import View
from apps.products.models.category import Category
from apps.products.models.product import Product
from django.contrib import messages

class AddProductView(View):
    template_name = 'admin_panel/products/add.html'

    def get(self,request):
        if not (request.user.is_authenticated and request.user.is_admin):
            return redirect('admin_login')
        categories=Category.objects.all()
        return render(request,self.template_name,{'categories':categories})
    
    def post(self,request):
        if not (request.user.is_authenticated and request.user.is_admin):
            return redirect('admin_login')
        
        try:
            product = Product.objects.create(
                name = request.POST['name'],
                category = request.POST['category'],
                price = request.POST['price'],
                descruption = request.POST['descruption'],
                stock_qauntity = request.POST['stock_quantity'],
            )
            if 'image' in request.FILES:
                product.image=request.FILES['image']
                product.save()
                messages.success(request,'Product added successfully')
                return redirect('admin_products')
        except Exception as e:
            messages.error(request,f'Erro:{str(e)}')
            return redirect('admin_add_product')
        

        
