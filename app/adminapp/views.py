from django.views import View
from django.views.generic import TemplateView,ListView, CreateView,UpdateView
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app.products.models import Product, Category
from app.orders.models import Order
from app.adminapp.forms import AdminLoginForm,ProductForm
from app.adminapp.decorators import admin_required
from django.utils.decorators import method_decorator

class AdminLoginView(View):
    template_name='admin/login.html'
    def get(self, request):
        form = AdminLoginForm()
        return render(request, self.template_name,{'form':form})
    
    def post(self, request):
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            user =authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            if user and hasattr(user,'userprofile') and user.userprofile.is_admin:
                login(request, user)
                return redirect('admin_dashboard')
            messages.error(request,'Invalid credentials or not an admin. ')
        return render(request,self.template_name, {'form':form})
    
class AdminLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('admin_login')
    
@method_decorator(admin_required, name='dispatch')
class DashboardView(ListView):
    model=Product
    template_name ='admin/dashboard.html'
    context_object_name='products'

@method_decorator(admin_required,name='dispatch')
class AddItemView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'admin/add_item.html'
    success_url = reverse_lazy('admin_dashboard')

@method_decorator(admin_required, name='dispatch')
class UpdateItemView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'admin/update_item.html'
    success_url = reverse_lazy('admin_dashboard')

@method_decorator(admin_required, name='dispatch')
class ViewOrderView(ListView):
    model = Order
    template_name = 'admin/view_orders.html'
    context_object_name = 'orders'
    ordering = ['-created_at']


