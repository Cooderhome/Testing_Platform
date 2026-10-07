from django.shortcuts import redirect, render
from .models import TestingSession
from accounts.models import User

def create_session(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        title = request.POST.get('title')
        user = request.user if request.user.is_authenticated else User.objects.first()
        if project_id and title:
            TestingSession.objects.create(
                project_id=project_id, title=title, tester=user, status='Active'
            )
    return redirect('dashboard')

def session_list(request):
    sessions = TestingSession.objects.all().order_by('-started_at')
    return render(request, 'session_list.html', {'sessions': sessions})

def test_case_list(request):
    from .models import TestCase
    test_cases = TestCase.objects.all()
    return render(request, 'test_case_list.html', {'test_cases': test_cases})
