from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^worklogger/', include('worklogger.urls', namespace='log')),
    url(r'', include('worklogger.urls', namespace='log')),
]
