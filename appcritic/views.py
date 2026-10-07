from django.shortcuts import render
from projects.models import Project
from findings.models import Finding

def dashboard(request):
    projects = Project.objects.all().order_by('-created_at')[:5]
    total_projects = Project.objects.count()
    open_findings = Finding.objects.exclude(status__in=['CLOSED', 'VERIFIED', 'FIXED', 'WONT_FIX', 'DUPLICATE']).count()
    recent_findings = Finding.objects.all().order_by('-created_at')[:5]
    
    context = {
        'recent_projects': projects,
        'total_projects': total_projects,
        'open_findings': open_findings,
        'recent_findings': recent_findings,
    }
    return render(request, 'dashboard.html', context)
