from django.db import models
from django.conf import settings

class Evidence(models.Model):
    EVIDENCE_TYPE_CHOICES = [
        ('SCREENSHOT', 'Screenshot'),
        ('VIDEO', 'Video'),
        ('DOCUMENT', 'Document'),
        ('LOG', 'Log'),
        ('OTHER', 'Other'),
    ]

    finding = models.ForeignKey('findings.Finding', on_delete=models.CASCADE, related_name='evidence')
    file = models.FileField(upload_to='evidence/')
    evidence_type = models.CharField(max_length=50, choices=EVIDENCE_TYPE_CHOICES, default='SCREENSHOT')
    description = models.TextField(blank=True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='uploaded_evidence')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_evidence_type_display()} for Finding {self.finding_id}"
