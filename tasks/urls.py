from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('task/details/<int:pk>/', TaskDetailView.as_view(), name="taskDetails"),
    path('task-completed-toggle/<int:pk>/', ToggleCompleted.as_view(), name="ToggleCompleted"),
]