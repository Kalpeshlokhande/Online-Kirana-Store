from django.shortcuts import redirect
from django.views import View

class AdminLogooutView(View):
    def get(self,request):
        request.session.flush()
        return redirect('aadmin_login')
