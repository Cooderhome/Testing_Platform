from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_center, name='report_center'),
    path('generate/', views.generate_report, name='generate_report'),
    path('<int:pk>/', views.view_report, name='view_report'),
]
