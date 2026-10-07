from rest_framework import viewsets, views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import (
    ProjectSerializer, TestingSessionSerializer, FindingSerializer, EvidenceSerializer
)
from projects.models import Project
from testing.models import TestingSession
from findings.models import Finding
from evidence.models import Evidence

class LoginView(views.APIView):
    permission_classes = []
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.id, 'username': user.username})
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TestingSessionViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TestingSessionSerializer
    
    def get_queryset(self):
        # For MVP, return all active sessions so any tester can join them
        return TestingSession.objects.filter(status='Active')

import base64
from django.core.files.base import ContentFile

class FindingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Finding.objects.all()
    serializer_class = FindingSerializer

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)

    def create(self, request, *args, **kwargs):
        screenshot_data = request.data.pop('screenshot_data', None)
        response = super().create(request, *args, **kwargs)
        
        if screenshot_data and screenshot_data.startswith('data:image'):
            try:
                format, imgstr = screenshot_data.split(';base64,')
                ext = format.split('/')[-1]
                data = ContentFile(base64.b64decode(imgstr), name=f'screenshot_{response.data["id"]}.{ext}')
                Evidence.objects.create(
                    finding_id=response.data['id'],
                    file=data,
                    evidence_type='SCREENSHOT',
                    uploaded_by=request.user
                )
            except Exception as e:
                print("Failed to save screenshot:", e)
        return response

class EvidenceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Evidence.objects.all()
    serializer_class = EvidenceSerializer

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)
