from django.utils import timezone
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages

from .models import *
from .forms import *

class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:

            context = {}

            # Get the current datetime
            current_datetime = timezone.now()
            tasks = Task.objects.filter(user=request.user, due_date__gt=current_datetime).order_by('is_completed')
            context['tasks'] = tasks

            return render(request, 'home.html', context)
        else:
            return redirect('login')
        

class TaskDetailView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            task = Task.objects.get(pk=pk)

            task_form = TaskForm(instance=task)
            image_formset = TaskImageFormSet(instance=task)
            return render(request, 'tasks/tasks-details.html', {'task': task, 'task_form': task_form, 'image_formset': image_formset})
        
    def post(self, request, pk):
        if request.user.is_authenticated:
            task = Task.objects.get(pk=pk)
            task_form = TaskForm(request.POST, instance=task)
            image_formset = TaskImageFormSet(request.POST, request.FILES, instance=task)
            if task_form.is_valid() and image_formset.is_valid():
                task_form.save()
                image_formset.save()
                messages.success(request, "Task updated successfully")
                return redirect(request.META.get('HTTP_REFERER'))
            messages.error(request, "Problems with update")
            return render(request, 'tasks/tasks-details.html', {'task': task, 'task_form': task_form, 'image_formset': image_formset})
        else:
            return redirect('login')
            