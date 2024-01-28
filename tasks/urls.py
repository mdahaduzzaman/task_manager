from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register('api/tasks', TaskViewSet, basename="tasks")

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('task/details/<int:pk>/', TaskDetailView.as_view(), name="taskDetails"),
    path('delete-task/<int:pk>/', DeleteTaskView.as_view(), name="DeleteTaskView"),
    path('task-completed-toggle/<int:pk>/', ToggleCompleted.as_view(), name="ToggleCompleted"),

    path('search-by-title/', SearchTitleView.as_view(), name="SearchTitleView"),
    path('filter-task/', FilterTaskView.as_view(), name="FilterTaskView"),
    path('expired-tasks/', ExpiredTaskView.as_view(), name="ExpiredTaskView"),
]

urlpatterns += router.urls