from django.conf.urls import url

from .views import TaskListView, TaskUpdateView, TaskDeleteView, TaskCreateView

urlpatterns = [
    url(r'^$', TaskListView.as_view()),
    url(r'^update/$', TaskUpdateView.as_view()),
    url(r'^create/$', TaskCreateView.as_view()),
    url(r'^delete/(?P<id>\d+)$', TaskDeleteView.as_view()),
]
