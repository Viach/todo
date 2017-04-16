from django.views.generic import TemplateView


class TaskListView(TemplateView):

    template_name = 'tasks_list.html'
