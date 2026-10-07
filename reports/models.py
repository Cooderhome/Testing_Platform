from django.db import models
from django.conf import settings

class Report(models.Model):
    REPORT_TYPES = [
        ('EXECUTIVE', 'Executive Report'),
        ('DEVELOPER', 'Developer Report'),
        ('QA', 'QA Report'),
        ('FULL', 'Full Project Report'),
    ]

    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='reports')
    testing_session = models.ForeignKey('testing.TestingSession', on_delete=models.SET_NULL, null=True, blank=True)
    report_type = models.CharField(max_length=50, choices=REPORT_TYPES, default='EXECUTIVE')
    
    title = models.CharField(max_length=255)
    prepared_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    confidentiality_label = models.CharField(max_length=100, default='Internal Use Only')
    
    executive_summary = models.TextField(blank=True)
    recommendations = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_report_type_display()})"
