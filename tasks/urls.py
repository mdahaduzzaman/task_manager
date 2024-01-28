from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('task/details/<int:pk>/', TaskDetailView.as_view(), name="taskDetails"),
    path('delete-task/<int:pk>/', DeleteTaskView.as_view(), name="DeleteTaskView"),
    path('task-completed-toggle/<int:pk>/', ToggleCompleted.as_view(), name="ToggleCompleted"),

    path('search-by-title/', SearchTitleView.as_view(), name="SearchTitleView"),
    path('expired-tasks/', ExpiredTaskView.as_view(), name="ExpiredTaskView"),
]