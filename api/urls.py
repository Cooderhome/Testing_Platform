from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, ProjectViewSet, TestingSessionViewSet, FindingViewSet, EvidenceViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'sessions', TestingSessionViewSet, basename='session')
router.register(r'findings', FindingViewSet)
router.register(r'evidence', EvidenceViewSet)

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='api-login'),
    path('', include(router.urls)),
]
