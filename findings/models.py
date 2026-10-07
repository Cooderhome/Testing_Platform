from django.db import models
from django.conf import settings

class Finding(models.Model):
    CATEGORY_CHOICES = [
        ('BUG', 'Bug'),
        ('USABILITY', 'Usability'),
        ('UI_UX', 'UI/UX'),
        ('DATA_QUALITY', 'Data Quality'),
        ('PERFORMANCE', 'Performance'),
        ('ACCESSIBILITY', 'Accessibility'),
        ('SECURITY', 'Security'),
        ('FUNCTIONAL', 'Functional'),
        ('REQUIREMENT', 'Requirement'),
        ('IMPROVEMENT', 'Improvement'),
        ('OTHER', 'Other'),
    ]

    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('TRIAGED', 'Triaged'),
        ('ASSIGNED', 'Assigned'),
        ('IN_PROGRESS', 'In Progress'),
        ('FIXED', 'Fixed'),
        ('READY_FOR_RETEST', 'Ready for Retest'),
        ('RETESTING', 'Retesting'),
        ('VERIFIED', 'Verified'),
        ('REOPENED', 'Reopened'),
        ('CLOSED', 'Closed'),
        ('WONT_FIX', 'Won\'t Fix'),
        ('DUPLICATE', 'Duplicate'),
    ]

    SEVERITY_CHOICES = [
        ('CRITICAL', 'Critical'),
        ('HIGH', 'High'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
        ('INFORMATIONAL', 'Informational'),
    ]

    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='findings')
    testing_session = models.ForeignKey('testing.TestingSession', on_delete=models.SET_NULL, null=True, blank=True, related_name='findings')
    module = models.ForeignKey('testing.Module', on_delete=models.SET_NULL, null=True, blank=True, related_name='findings')
    
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='reported_findings')
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_findings')
    
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='BUG')
    severity = models.CharField(max_length=50, choices=SEVERITY_CHOICES, default='MEDIUM')
    priority = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='NEW')
    
    expected_behavior = models.TextField(blank=True)
    actual_behavior = models.TextField(blank=True)
    recommendation = models.TextField(blank=True)
    
    page_url = models.URLField(max_length=2000, blank=True)
    page_title = models.CharField(max_length=500, blank=True)
    
    element_identifier = models.CharField(max_length=255, blank=True)
    element_text = models.TextField(blank=True)
    element_tag = models.CharField(max_length=50, blank=True)
    element_selector = models.TextField(blank=True)
    
    x_position = models.IntegerField(null=True, blank=True)
    y_position = models.IntegerField(null=True, blank=True)
    viewport_width = models.IntegerField(null=True, blank=True)
    viewport_height = models.IntegerField(null=True, blank=True)
    
    browser = models.CharField(max_length=100, blank=True)
    operating_system = models.CharField(max_length=100, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    verified_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.project.name} - {self.pk} - {self.title or 'Untitled'}"

class Annotation(models.Model):
    finding = models.OneToOneField(Finding, on_delete=models.CASCADE, related_name='annotation')
    page_url = models.URLField(max_length=2000)
    page_title = models.CharField(max_length=500, blank=True)
    selector = models.TextField()
    element_tag = models.CharField(max_length=50, blank=True)
    element_text = models.TextField(blank=True)
    x = models.FloatField(null=True, blank=True)
    y = models.FloatField(null=True, blank=True)
    width = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    viewport_width = models.IntegerField(null=True, blank=True)
    viewport_height = models.IntegerField(null=True, blank=True)
    scroll_x = models.IntegerField(null=True, blank=True)
    scroll_y = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Annotation for Finding {self.finding_id}"

class Comment(models.Model):
    finding = models.ForeignKey(Finding, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} on Finding {self.finding_id}"
