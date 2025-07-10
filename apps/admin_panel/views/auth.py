from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import User
from django.contrib.auth import authenticate, login

class AdminLoginView(View):
    template_name = 'admin_panel/login.html'

    def get(self, request):
        if request.user.is_authenticated and request.user.is_admin:
            return redirect('admin_dashboard')
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        
        if user is not None and user.is_admin:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            request.session['admin_access_token'] = str(refresh.access_token)
            return redirect('admin_dashboard')
        
        messages.error(request, 'Invalid credentials or not an admin')
        return render(request, self.template_name)

class AdminLogoutView(View):
    def get(self, request):
        request.session.flush()
        return redirect('admin_login')

class AdminDashboardView(View):
    template_name = 'admin_panel/dashboard.html'

    def get(self, request):
        if not (request.user.is_authenticated and request.user.is_admin):
            return redirect('admin_login')
        return render(request, self.template_name)
    
    