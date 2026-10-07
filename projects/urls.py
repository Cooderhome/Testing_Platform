from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('create/', views.create_project, name='create_project'),
    path('<int:pk>/update/', views.update_project, name='update_project'),
    path('<int:pk>/delete/', views.delete_project, name='delete_project'),
]
