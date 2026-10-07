from django.db import models
from django.conf import settings

class FindingStatusHistory(models.Model):
    finding = models.ForeignKey('findings.Finding', on_delete=models.CASCADE, related_name='status_history')
    old_status = models.CharField(max_length=50)
    new_status = models.CharField(max_length=50)
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.finding.id}: {self.old_status} -> {self.new_status}"
