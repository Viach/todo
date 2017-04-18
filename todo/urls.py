from django.conf.urls import url, include
from django.conf.urls.static import static

from django.contrib import admin

api_urls = [
    url(r'^tasks/', include('app_todo.api.urls')),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),
    url(r'^$', include('app_todo.urls')),
]
