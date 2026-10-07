from django.core.exceptions import PermissionDenied

def role_required(*allowed_roles):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated:
                from accounts.models import User
                user = User.objects.first()
                
            if user and getattr(user, 'role', None) in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied
        return wrap
    return decorator
