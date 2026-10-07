from django.shortcuts import redirect, render
from .models import Project
from accounts.models import User

def create_project(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        target_url = request.POST.get('target_url')
        environment = request.POST.get('environment', 'Production')
        user = request.user if request.user.is_authenticated else User.objects.first()
        org = getattr(user, 'organization', None)
        if not org:
            from organizations.models import Organization
            org, _ = Organization.objects.get_or_create(name="Default Org", defaults={'domain': 'default.com'})
            user.organization = org
            user.save()
            
        Project.objects.create(
            name=name, target_url=target_url, environment=environment, 
            created_by=user, organization=org
        )
    return redirect('dashboard')

def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'project_list.html', {'projects': projects})

from django.shortcuts import get_object_or_404

def update_project(request, pk):
    if request.method == 'POST':
        project = get_object_or_404(Project, pk=pk)
        project.name = request.POST.get('name')
        project.target_url = request.POST.get('target_url')
        project.environment = request.POST.get('environment')
        project.save()
    return redirect('project_list')

def delete_project(request, pk):
    if request.method == 'POST':
        project = get_object_or_404(Project, pk=pk)
        project.delete()
    return redirect('project_list')
