from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse

urlpatterns = [
    # Examples:
    # url(r'^$', 'work_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^worklogger/', include('worklogger.urls', namespace='log')),
    url(r'', include('worklogger.urls', namespace='log')),
]
