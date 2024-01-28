from django.contrib import admin
from django.db.models import Case, When

from .models import *


@admin.register(TaskImage)
class TaskImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'task']


class TaskImageInline(admin.StackedInline):
    model = TaskImage

        
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'due_date', 'priority', 'is_completed']
    def get_queryset(self, request):
        # Get the original queryset
        queryset = super().get_queryset(request)
        # Custom sorting: high, medium, low
        queryset = queryset.annotate(
            priority_order=Case(
                When(priority='high', then=1),
                When(priority='medium', then=2),
                When(priority='low', then=3),
                default=4,  # Any other priorities will be sorted at the end
                output_field=models.IntegerField(),
            )
        ).order_by('priority_order')
        return queryset

    inlines = [
        TaskImageInline,
    ]