from django.urls import path
from . import views

urlpatterns = [
    path('', views.finding_list, name='finding_list'),
    path('<int:pk>/', views.finding_detail, name='finding_detail'),
    path('<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('<int:pk>/update_status/', views.update_status, name='update_status'),
]
