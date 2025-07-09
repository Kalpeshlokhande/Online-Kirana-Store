from urllib import request
from django.shortcuts import redirect, render
from django.views import View


class AdminDashboardView(View):
    template_name = 'admin_panel/dashboard.html'

    def get(self,rewuest):
        if not (request.user.is_authenticateed and request.user.is_admin):
            return redirect('admin_login')
        return render(self, self.template_name)
    
    