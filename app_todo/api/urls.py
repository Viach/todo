from django.conf.urls import url

from .views import TaskListView, TaskUpdateView, TaskDeleteView, TaskCreateView, \
    get_tasks_choices

urlpatterns = [
    url(r'^$', TaskListView.as_view()),
    url(r'^update/$', TaskUpdateView.as_view()),
    url(r'^create/$', TaskCreateView.as_view()),
    url(r'^get_tasks_choices/$', get_tasks_choices, name='get_tasks_choices'),
    url(r'^delete/(?P<id>\d+)$', TaskDeleteView.as_view()),
]
