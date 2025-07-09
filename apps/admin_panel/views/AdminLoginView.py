from django.contrib import messages
from django.shortcuts import redirect,render
from django.views import View
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken

class AdminLoginView(View):
    template_name = 'admin_panel/login.html'

    def get(self,request):
        if request.user.is_authenticated and request.user.is_admin:
            return redirect('admin_dashboard')
        return render(request,self.template_name)
    
    def post(self,request):
        email = request.POST['email']
        password =request.POST['password']
        user=authenticate(username=email,password=password)

        if user is not None and user.is_admin:
            login(request,user)
            refresh = RefreshToken.for_user(user)
            request.session['admin_access_token'] =str(refresh.access_token)
            return redirect('admin_dashboard')
        
        messages.error(request, 'Invalid credential or not and admin')
        return render(request, self.template_name)
    
    