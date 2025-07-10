from django.views.generic import FormView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from apps.admin_panel.forms.AdminLoginForm import AdminLoginForm

class AdminLoginView(FormView):
    template_name = 'admin_panel/login.html'
    form_class = AdminLoginForm
    success_url = reverse_lazy('admin_panel:dashboard')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_admin:
            return redirect('admin_panel:dashboard')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(self.request, email=email, password=password)
        if user and user.is_admin:
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            return render(self.request, self.template_name, {
                'form': form,
                'error': 'Invalid admin credentials',
            })