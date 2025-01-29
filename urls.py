from django.urls import path
from .views import (
    RegistView, HomeView,TaskListView,TaskDetailView)

app_name = 'todo'
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('regist_task/',RegistView.as_view(),name='regist_task'),
    path('task_list/',TaskListView.as_view(),name='task_list'),
    path('task_detail/<int:pk>/',TaskDetailView.as_view(),name='task_detail'),
    ]
