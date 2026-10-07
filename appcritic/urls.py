"""
URL configuration for appcritic project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('project/', include('projects.urls')),
    path('session/', include('testing.urls')),
    path('finding/', include('findings.urls')),
    path('users/', include('accounts.urls')),
    path('org/', include('organizations.urls')),
    path('reports/', include('reports.urls')),
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
