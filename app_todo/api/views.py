from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from .serializers import TaskSerializer
from app_todo.models import Task


class TaskListView(ListAPIView):
    model = Task
    serializer_class = TaskSerializer    

    def get_queryset(self):
        return Task.objects.all()


class TaskUpdateView(UpdateAPIView):    
    model = Task
    serializer_class = TaskSerializer
    
    def get_object(self, *args, **kwargs):        
        return Task.objects.get(pk=self.request.data['id'])


class TaskDeleteView(DestroyAPIView):
    model = Task
    serializer_class = TaskSerializer
    
    def get_object(self, *args, **kwargs):           
        return Task.objects.get(pk=self.kwargs['id'])


class TaskCreateView(CreateAPIView):
    model = Task
    serializer_class = TaskSerializer
    
    def get_object(self, *args, **kwargs):        
        return Task.objects.get(pk=self.request.data['id'])