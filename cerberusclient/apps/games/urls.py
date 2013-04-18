from django.conf.urls import patterns, include, url
from games import views

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^(?P<package_id>\d+)/$', views.package_action),
)