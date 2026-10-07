from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('TESTER', 'Tester'),
        ('DEVELOPER', 'Developer'),
        ('MANAGER', 'Manager'),
        ('EXECUTIVE', 'Executive'),
        ('VIEWER', 'Viewer'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='TESTER')
    organization = models.ForeignKey(
        'organizations.Organization', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='users'
    )

    def __str__(self):
        return self.username
