import json
from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from django.http import JsonResponse
from django.db.models import Q
from .serializers import TaskSerializer
from app_todo.models import Task


class TaskListView(ListAPIView):
    model = Task
    serializer_class = TaskSerializer    

    def get_queryset(self):        
        filter_categories = json.loads(self.request.query_params.get('filter_categories'))
        filter_categories = {i for i in filter_categories if filter_categories[i]}
        filter_priorities = json.loads(self.request.query_params.get('filter_priorities'))
        filter_priorities = {i for i in filter_priorities if filter_priorities[i]}
        filter_done_tasks = json.loads(self.request.query_params.get('filter_done_tasks'))
        filter_done_tasks = filter_done_tasks if filter_done_tasks else None        
        order_tasks = json.loads(self.request.query_params.get('order_tasks'))
        order_tasks = '' if order_tasks else '-'
        return Task.objects.filter(category__in=filter_categories, 
                                   priority__in=filter_priorities,
                                   ).filter(~Q(done=filter_done_tasks)
                                   ).order_by(order_tasks + 'should_do_before')


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

def get_tasks_choices(request):
    categories = {category[1]:category[0] for category in Task.TODO_CATEGORIES_CHOICES}
    priorities = {priority[1]:priority[0] for priority in Task.TODO_PRIORITIES_CHOICES}
    return JsonResponse(data={'categories': categories, 
                              'priorities': priorities})