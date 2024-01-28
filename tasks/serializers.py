from rest_framework import serializers
from .models import Task, TaskImage

class TaskImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskImage
        fields = ('image',)

class TaskSerializer(serializers.ModelSerializer):
    images = TaskImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length=10000000, allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'description', 'due_date', 'priority', 'is_completed', 'created_at', 'updated_at', 'images', 'uploaded_images')

    def create(self, validated_data):
        images_data = validated_data.pop('uploaded_images')
        task = Task.objects.create(**validated_data)
        for image in images_data:
            TaskImage.objects.create(task=task, image=image)
        return task

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)

        uploaded_images_data = validated_data.pop('uploaded_images')
        existing_images = instance.images.all()

        # Delete images not present in uploaded_images
        for existing_image in existing_images:
            if existing_image.image not in uploaded_images_data:
                existing_image.delete()

        # Create TaskImage objects only if they don't already exist
        for image_data in uploaded_images_data:
            image_exists = False
            for existing_image in existing_images:
                if existing_image.image == image_data:
                    image_exists = True
                    break
            
            if not image_exists:
                TaskImage.objects.create(task=instance, image=image_data)

        instance.save()
        return instance

