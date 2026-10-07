from rest_framework import serializers
from accounts.models import User
from projects.models import Project
from testing.models import TestingSession
from findings.models import Finding, Annotation
from evidence.models import Evidence

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'target_url', 'environment']

class TestingSessionSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    class Meta:
        model = TestingSession
        fields = ['id', 'project', 'title', 'environment', 'browser', 'operating_system']

class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        exclude = ['finding']

class FindingSerializer(serializers.ModelSerializer):
    annotation = AnnotationSerializer(required=False)
    project = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Finding
        fields = [
            'id', 'project', 'testing_session', 'title', 'description', 
            'category', 'severity', 'status', 'page_url', 'page_title',
            'element_text', 'element_tag', 'element_selector', 'annotation'
        ]

    def create(self, validated_data):
        annotation_data = validated_data.pop('annotation', None)
        if 'testing_session' in validated_data and validated_data['testing_session']:
            validated_data['project'] = validated_data['testing_session'].project
        finding = Finding.objects.create(**validated_data)
        if annotation_data:
            Annotation.objects.create(finding=finding, **annotation_data)
        return finding

class EvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidence
        fields = ['id', 'finding', 'file', 'evidence_type', 'description']
