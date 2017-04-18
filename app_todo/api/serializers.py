from rest_framework import serializers
from app_todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    category = serializers.ChoiceField(choices=Task.TODO_CATEGORIES_CHOICES,
                                       default=Task.WORK)
    category_display = serializers.SerializerMethodField('get_task_category_display')

    priority = serializers.ChoiceField(choices=Task.TODO_PRIORITIES_CHOICES,
                                       default=Task.NORMAL)
    priority_display = serializers.SerializerMethodField('get_task_priority_display')

    def get_task_category_display(self, obj):
        return obj.get_category_display()

    def get_task_priority_display(self, obj):
        return obj.get_priority_display()

    class Meta:
        model = Task
        fields = '__all__'
