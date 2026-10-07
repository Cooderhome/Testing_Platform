from django.shortcuts import render
from accounts.decorators import role_required

from accounts.models import User

@role_required('ADMIN')
def settings_view(request):
    user = request.user if request.user.is_authenticated else User.objects.first()
    return render(request, 'settings.html', {'settings_user': user})
