
from django.urls import path

from . import views

urlpatterns = [
    path('tasks/list', views.task_list, name='task_list'),
    path('tasks/create/', views.create_task, name='create_task'),
]