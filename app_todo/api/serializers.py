from rest_framework import serializers
from app_todo.models import Task

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = '__all__'