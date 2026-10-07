from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import User
from .decorators import role_required

@role_required('ADMIN', 'MANAGER')
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

@role_required('ADMIN', 'MANAGER')
def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role', 'TESTER')
        
        current_user = request.user if request.user.is_authenticated else User.objects.first()
        org = getattr(current_user, 'organization', None)
        
        if not User.objects.filter(username=username).exists():
            User.objects.create(
                username=username,
                email=email,
                password=make_password(password),
                role=role,
                organization=org
            )
    return redirect('user_list')

def profile_view(request):
    user = request.user if request.user.is_authenticated else User.objects.first()
    return render(request, 'profile.html', {'profile_user': user})
