from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Report
from projects.models import Project
from findings.models import Finding
from accounts.models import User

def report_center(request):
    reports = Report.objects.all().order_by('-created_at')
    projects = Project.objects.all()
    return render(request, 'report_center.html', {
        'reports': reports,
        'projects': projects
    })

def generate_report(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        report_type = request.POST.get('report_type')
        title = request.POST.get('title')
        
        project = get_object_or_404(Project, id=project_id)
        user = request.user if request.user.is_authenticated else User.objects.first()
        
        report = Report.objects.create(
            project=project,
            report_type=report_type,
            title=title,
            prepared_by=user
        )
        return redirect('view_report', pk=report.id)
    return redirect('report_center')

def view_report(request, pk):
    report = get_object_or_404(Report, pk=pk)
    findings = Finding.objects.filter(project=report.project).exclude(status__in=['CLOSED', 'WONT_FIX', 'DUPLICATE'])
    
    if report.report_type == 'EXECUTIVE':
        stats = {
            'critical': findings.filter(severity='CRITICAL').count(),
            'high': findings.filter(severity='HIGH').count(),
            'medium': findings.filter(severity='MEDIUM').count(),
            'total': findings.count(),
        }
        return render(request, 'executive_report.html', {'report': report, 'stats': stats})
    else:
        return render(request, 'developer_report.html', {'report': report, 'findings': findings})
