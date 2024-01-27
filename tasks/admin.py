from django.contrib import admin
from .models import *


@admin.register(TaskImage)
class TaskImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'task']


class TaskImageInline(admin.StackedInline):
    model = TaskImage

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'due_date', 'is_completed']
    inlines = [
        TaskImageInline,
    ]