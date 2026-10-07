from django.urls import path
from . import views

urlpatterns = [
    path('', views.session_list, name='session_list'),
    path('cases/', views.test_case_list, name='test_case_list'),
    path('create/', views.create_session, name='create_session'),
]
