from django.db import models
from django.conf import settings

class Project(models.Model):
    ENVIRONMENT_CHOICES = [
        ('Development', 'Development'),
        ('Testing', 'Testing'),
        ('Staging', 'Staging'),
        ('Production', 'Production'),
    ]
    organization = models.ForeignKey('organizations.Organization', on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    target_url = models.URLField()
    environment = models.CharField(max_length=50, choices=ENVIRONMENT_CHOICES, default='Testing')
    status = models.CharField(max_length=50, default='Active')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='created_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Application(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='applications')
    name = models.CharField(max_length=255)
    base_url = models.URLField()
    technology = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='owned_applications')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
