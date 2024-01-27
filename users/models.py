from django.db import models
from django.contrib.auth.models import AbstractUser

def user_avatar_upload_path(instance, filename):
    """
    A utility function to modify the image name for each user instance
    """
    return f'Users/Avatar/{instance.first_name or instance.username}_{instance.id}_{filename}'


class User(AbstractUser):
    """
    A Cutom User model to add profile picture to each user
    and overwrite the date_joined to created_at
    """
    date_joined = None
    avatar = models.ImageField(upload_to=user_avatar_upload_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'User'
        verbose_name = ('User')
        verbose_name_plural = ('Users')

    def delete(self, *args, **kwargs):
        # Delete the image file from the file system
        if self.avatar:
            storage, path = self.avatar.storage, self.avatar.path
            if path and storage.exists(path):
                storage.delete(path)
        # Call the superclass delete method to delete the instance
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        # Check if the user already has an avatar and if it's being updated
        if self.pk:
            try:
                old_user = User.objects.get(pk=self.pk)
                # Delete the old avatar file if it exists and the new avatar is different
                if self.avatar != old_user.avatar:
                    storage = old_user.avatar.storage
                    old_path = None
                    if old_user.avatar:
                        old_path = old_user.avatar.path
                    if old_path and storage.exists(old_path):
                        storage.delete(old_path)
            except User.DoesNotExist:
                pass
        # Call the superclass save method to save the instance
        super().save(*args, **kwargs)

