from django.conf.urls import patterns, include, url
from marketplace import views

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^(?P<package_id>\d+)/download/$', views.download),
    url(r'^(?P<package_id>\d+)/$', views.package_detail, name='package_detail'),
)