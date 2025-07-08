from django.shortcuts import redirect

def admin_required(view_func):
    def _wrapped_view(request,*args,**kwargs):
        if not request.user.is_authenticated or not hasattr(request.user, 'userprofile') or not request.user.userprofile.is_admin:
            return redirect('admin_login')
        return  view_func(request, *args ,**kwargs)
    return _wrapped_view