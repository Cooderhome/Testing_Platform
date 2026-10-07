from django.shortcuts import render, get_object_or_404, redirect
from .models import Finding, Comment
from audit.models import FindingStatusHistory
from accounts.models import User

def finding_detail(request, pk):
    finding = get_object_or_404(Finding, pk=pk)
    users = User.objects.filter(is_active=True)
    return render(request, 'finding_detail.html', {'finding': finding, 'users': users})

def add_comment(request, pk):
    if request.method == 'POST':
        finding = get_object_or_404(Finding, pk=pk)
        text = request.POST.get('text')
        user = request.user if request.user.is_authenticated else User.objects.first()
        if text and user:
            Comment.objects.create(finding=finding, user=user, text=text)
    return redirect('finding_detail', pk=pk)

def update_status(request, pk):
    if request.method == 'POST':
        finding = get_object_or_404(Finding, pk=pk)
        new_status = request.POST.get('status')
        assigned_to_id = request.POST.get('assigned_to')
        comment_text = request.POST.get('comment')
        
        user = request.user if request.user.is_authenticated else User.objects.first()

        if assigned_to_id:
            finding.assigned_to_id = assigned_to_id
        else:
            finding.assigned_to = None

        if new_status and new_status != finding.status:
            old_status = finding.status
            finding.status = new_status
            
            FindingStatusHistory.objects.create(
                finding=finding,
                old_status=old_status,
                new_status=new_status,
                changed_by=user,
                comment=comment_text or ''
            )
        
        finding.save()
    return redirect('finding_detail', pk=pk)

def finding_list(request):
    findings = Finding.objects.all().order_by('-created_at')
    return render(request, 'finding_list.html', {'findings': findings})
