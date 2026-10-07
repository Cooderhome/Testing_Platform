from django.core.management.base import BaseCommand
from accounts.models import User
from organizations.models import Organization
from projects.models import Project
from testing.models import Module, TestingSession
from findings.models import Finding
from django.utils import timezone

class Command(BaseCommand):
    help = 'Seeds the database with demo data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding demo data...')

        # Organization
        org, _ = Organization.objects.get_or_create(
            name='Acme Corp',
            defaults={'description': 'Demo Organization'}
        )

        # Users
        admin_user, _ = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'role': 'ADMIN',
                'organization': org,
                'is_staff': True,
                'is_superuser': True
            }
        )
        if admin_user.password == '':
            admin_user.set_password('admin123')
            admin_user.save()

        tester, _ = User.objects.get_or_create(
            username='tester_john',
            defaults={
                'email': 'john@example.com',
                'role': 'TESTER',
                'organization': org
            }
        )
        if tester.password == '':
            tester.set_password('tester123')
            tester.save()

        # Project
        project, _ = Project.objects.get_or_create(
            name='DataFusion Demo',
            defaults={
                'organization': org,
                'description': 'Data Discovery & Investigation Platform',
                'target_url': 'http://localhost:8000',
                'environment': 'Staging',
                'created_by': admin_user
            }
        )

        # Modules
        modules = ['Dashboard', 'Data Discovery', 'CDR Analytics', 'Investigation', 'Relationship Graph', 'Reports']
        for idx, m_name in enumerate(modules):
            Module.objects.get_or_create(
                project=project,
                name=m_name,
                defaults={'order': idx}
            )

        discovery_mod = Module.objects.get(project=project, name='Data Discovery')

        # Session
        session, _ = TestingSession.objects.get_or_create(
            project=project,
            title='DataFusion Regression Test — Build 2.4.0',
            defaults={
                'tester': tester,
                'started_at': timezone.now(),
                'status': 'Active',
                'environment': 'Staging',
                'browser': 'Chrome 116',
                'operating_system': 'Windows 11'
            }
        )

        # Findings
        Finding.objects.get_or_create(
            project=project,
            title='Search action is not sufficiently clear',
            defaults={
                'testing_session': session,
                'module': discovery_mod,
                'reporter': tester,
                'category': 'USABILITY',
                'severity': 'MEDIUM',
                'status': 'NEW',
                'description': 'The primary search action may not be immediately identifiable to a new user.',
                'recommendation': 'Improve visual prominence and labeling of the primary search action.',
                'page_url': 'http://localhost:8000/discovery',
                'element_text': 'Search',
            }
        )

        Finding.objects.get_or_create(
            project=project,
            title='Graph rendering fails on large datasets',
            defaults={
                'testing_session': session,
                'module': Module.objects.get(project=project, name='Relationship Graph'),
                'reporter': tester,
                'assigned_to': admin_user,
                'category': 'BUG',
                'severity': 'HIGH',
                'status': 'IN_PROGRESS',
                'description': 'Attempting to load more than 500 nodes crashes the canvas.',
                'page_url': 'http://localhost:8000/graph',
            }
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded demo data!'))
