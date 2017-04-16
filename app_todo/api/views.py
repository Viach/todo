from rest_framework.generics import ListAPIView

from .serializers import TaskSerializer
from app_todo.models import Task


class TaskListView(ListAPIView):
    serializer_class = TaskSerializer
    model = Task

    def get_queryset(self):
        return Task.objects.all()