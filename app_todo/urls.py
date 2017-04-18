from django.conf.urls import url, include
from app_todo.views import TaskListView

urlpatterns = [
    url(r'^$', TaskListView.as_view()),
]
