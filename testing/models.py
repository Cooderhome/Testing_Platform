from django.db import models
from django.conf import settings

class Module(models.Model):
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='modules')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.project.name} - {self.name}"

class TestingSession(models.Model):
    STATUS_CHOICES = [
        ('Planned', 'Planned'),
        ('Active', 'Active'),
        ('Paused', 'Paused'),
        ('Completed', 'Completed'),
        ('Archived', 'Archived'),
    ]
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='sessions')
    tester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='testing_sessions')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    started_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Planned')
    environment = models.CharField(max_length=100, blank=True)
    browser = models.CharField(max_length=100, blank=True)
    operating_system = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

class TestCase(models.Model):
    STATUS_CHOICES = [
        ('Draft', 'Draft'),
        ('Active', 'Active'),
        ('Deprecated', 'Deprecated'),
    ]
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='test_cases')
    module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True, blank=True, related_name='test_cases')
    title = models.CharField(max_length=255)
    objective = models.TextField(blank=True)
    preconditions = models.TextField(blank=True)
    test_data = models.TextField(blank=True)
    steps = models.TextField()
    expected_result = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')

    def __str__(self):
        return self.title
