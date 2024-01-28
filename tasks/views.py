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
            # Create a new task form
            task_form = TaskForm()
            image_formset = TaskImageFormSet()
            context['task_form'] = task_form
            context['image_formset'] = image_formset

            return render(request, 'home.html', context)
        else:
            return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            context = {}
            task_form = TaskForm(request.POST)
            image_formset = TaskImageFormSet(request.POST, request.FILES)
            if task_form.is_valid() and image_formset.is_valid():
                task_form.instance.user = request.user
                task_form.save()
                image_formset.save()
                messages.success(request, "Task Added successfully")
                return redirect(request.META.get('HTTP_REFERER'))
            
            # Get the current datetime
            current_datetime = timezone.now()
            tasks = Task.objects.filter(user=request.user, due_date__gt=current_datetime).order_by('is_completed')
            context['tasks'] = tasks
            context['task_form'] = task_form

            context['image_formset'] = image_formset

            messages.error(request, "Task cannot be added")

            return render(request, 'home.html', context)
            
        

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

class ToggleCompleted(View):
    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        if task.user == request.user:
            if task.is_completed:
                messages.warning(request, f"{task.title} marked as Incomplete.")
            else:
                messages.success(request, f"{task.title} marked as Complete.")

            task.is_completed = not task.is_completed

            task.save()
            return redirect("home")
        else:
            messages.error(request, "You're not authorized to change task.")


class SearchTitleView(View):
    def get(self, request):
        if request.user.is_authenticated:
            context = {}

            search_key = request.GET.get("search")
            tasks = Task.objects.filter(user=request.user, title__icontains = search_key)

            if len(tasks) == 0:
                messages.warning(request, "Not matched with any task title")
            else:
                messages.success(request, f"{len(tasks)} task match with {search_key}")

            context['tasks'] = tasks
            # Create a new task form
            task_form = TaskForm()
            image_formset = TaskImageFormSet()
            context['task_form'] = task_form
            context['image_formset'] = image_formset

            return render(request, 'home.html', context)

class ExpiredTaskView(View):
    def get(self, request):
        if request.user.is_authenticated:
            # Get the current datetime
            current_datetime = timezone.now()
            tasks = Task.objects.filter(user=request.user, due_date__lt=current_datetime).order_by('is_completed')
            context = {}

            context['tasks'] = tasks
            # Create a new task form
            task_form = TaskForm()
            image_formset = TaskImageFormSet()
            context['task_form'] = task_form
            context['image_formset'] = image_formset

            return render(request, 'home.html', context)

class DeleteTaskView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            task = Task.objects.get(pk=pk)
            if task.user != request.user:
                messages.error(request, "You don't have the permission to delete this task")
            else:
                messages.success(request, f"{task.title} deleted successfully.")
                task.delete()
                return redirect('home')
            return redirect(request.META.get('HTTP_REFERER'))
        
class FilterTaskView(View):
    def post(self, request):
        if request.user.is_authenticated:
            created_at = request.POST.get('created_at')
            due_date = request.POST.get('due_date')
            priority = request.POST.get('priority')
            is_completed = request.POST.get('is_completed') or False

            context = {}

            # Constructing the filter criteria based on received values
            filter_condition = {}
            filter_condition['user'] = request.user
            # Add filter conditions for received values
            if created_at:
                filter_condition['created_at__lt'] = created_at
            if due_date:
                filter_condition['due_date__lt'] = due_date
            if priority is not None:
                filter_condition['priority'] = priority
            if is_completed is not None:
                filter_condition['is_completed'] = is_completed

            # Filtering tasks based on the constructed filter condition
            tasks = Task.objects.filter(**filter_condition)

            if len(tasks) == 0:
                messages.warning(request, "Not matched with any task")
            else:
                messages.success(request, f"{len(tasks)} task match with the criteria")

            context['tasks'] = tasks
            # Create a new task form
            task_form = TaskForm()
            image_formset = TaskImageFormSet()
            context['task_form'] = task_form
            context['image_formset'] = image_formset

            return render(request, 'home.html', context)

        return redirect(request.META.get('HTTP_REFERER'))