from django.db import models
from users.models import User

def task_image_upload_path(instance, filename):
    """
    A utility function to modify the image name for each Task instance
    """
    # Extracting the Task ID from the instance's task field
    task_id = instance.task.id
    # Generating the upload path including the Task ID
    return f'Tasks/Image/{task_id}_{filename}'


class Task(models.Model):
    """
    A Task model to represent a Task corresponding to a registered user
    where every field is required
    """

    # priority choices to make this as option into priority field
    priority_choices = (
        ('low', 'low'),
        ('medium', 'medium'),
        ('high', 'high')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=priority_choices, default='low')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Task"
        verbose_name = ('Task')
        verbose_name_plural = ('Tasks')

    def __str__(self) -> str:
        return self.title



class TaskImage(models.Model):
    """
    Task Image model to store multiple image in a single Task
    """

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name = "images")
    image = models.ImageField(upload_to=task_image_upload_path)

    class Meta:
        db_table = "TaskImage"
        verbose_name = ('TaskImage')
        verbose_name_plural = ('TaskImages')

    
    def delete(self, *args, **kwargs):
        # Delete the image file from the file system
        if self.image:
            storage, path = self.image.storage, self.image.path
            if path and storage.exists(path):
                storage.delete(path)
        # Call the superclass delete method to delete the instance
        super().delete(*args, **kwargs)