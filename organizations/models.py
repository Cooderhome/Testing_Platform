from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='org_logos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
