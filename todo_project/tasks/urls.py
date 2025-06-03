from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.task_add, name='task_add'),
    path('edit/<int:pk>/', views.task_edit, name='task_edit'),
    path('toggle/<int:pk>/', views.task_toggle, name='task_toggle'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
]
