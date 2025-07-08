from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from app.users.models import UserProfile
from app.products.models import Product, Category
from app.orders.models import Order
from .forms import AdminRegisterForm, AdminLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not hasattr(request.user, 'userprofile') or not request.user.userprofile.is_admin:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper

class AdminRegisterView(View):
    def get(self, request):
        form = AdminRegisterForm()
        return render(request, 'admin/register.html', {'form': form})
    def post(self, request):
        form = AdminRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            UserProfile.objects.create(user=user, is_admin=True)
            return redirect('adminapp:login')
        return render(request, 'admin/register.html', {'form': form})

class AdminLoginView(View):
    def get(self, request):
        form = AdminLoginForm()
        return render(request, 'admin/login.html', {'form': form})
    def post(self, request):
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user and hasattr(user, 'userprofile') and user.userprofile.is_admin:
                login(request, user)
                return redirect('adminapp:dashboard')
            form.add_error(None, 'Invalid credentials or not an admin')
        return render(request, 'admin/login.html', {'form': form})

class AdminLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('adminapp:login')

class AdminDashboardView(LoginRequiredMixin, View):
    login_url = reverse_lazy('adminapp:login')
    def get(self, request):
        if not request.user.userprofile.is_admin:
            raise PermissionDenied
        orders = Order.objects.all().order_by('-created_at')
        return render(request, 'admin/dashboard.html', {'orders': orders})

class AddItemView(LoginRequiredMixin, View):
    login_url = reverse_lazy('adminapp:login')
    def get(self, request):
        if not request.user.userprofile.is_admin:
            raise PermissionDenied
        categories = Category.objects.all()
        return render(request, 'admin/add_item.html', {'categories': categories})
    def post(self, request):
        # Basic form handling
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('description')
        cat_id = request.POST.get('category')
        stock = request.POST.get('stock_quantity')
        image = request.FILES.get('image')
        category = Category.objects.get(id=cat_id)
        Product.objects.create(name=name, price=price, description=desc, category=category, stock_quantity=stock, image=image)
        return redirect('adminapp:dashboard')

class UpdateItemView(LoginRequiredMixin, View):
    login_url = reverse_lazy('adminapp:login')
    def get(self, request, pk):
        if not request.user.userprofile.is_admin:
            raise PermissionDenied
        product = Product.objects.get(pk=pk)
        categories = Category.objects.all()
        return render(request, 'admin/update_item.html', {'product': product, 'categories': categories})
    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        product.category = Category.objects.get(id=request.POST.get('category'))
        product.stock_quantity = request.POST.get('stock_quantity')
        if request.FILES.get('image'):
            product.image = request.FILES.get('image')
        product.save()
        return redirect('adminapp:dashboard')

class ViewOrdersView(LoginRequiredMixin, View):
    login_url = reverse_lazy('adminapp:login')
    def get(self, request):
        if not request.user.userprofile.is_admin:
            raise PermissionDenied
        orders = Order.objects.all().order_by('-created_at')
        
        