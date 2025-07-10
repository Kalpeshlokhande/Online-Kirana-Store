from django.shortcuts import redirect
from django.views import View

class AdminLogoutView(View):
    def get(self, request):
        request.session.flush()
        return redirect('admin_login')
