from django.conf.urls import url

from . import views


urlpatterns = [
    # ex: /worklogger/
    url(r'^$', views.index, name='index'),
    # ex: /worklogger/login/
    url(r'^login/$', views.login_view, name='login'),
    # ex: /worklogger/logout/
    url(r'^logout/$', views.logout_view, name='logout'),

    url(r'^logs/$', views.logs, name='logs'),
]
