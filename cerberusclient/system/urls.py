from django.conf.urls import patterns, include, url
from system import views

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^recent_notifs/$', views.getRecentNotifs),
    url(r'^check_notifs/$', views.checkForNotifs),
    url(r'^mark_as_seen/$', views.markAsSeen),
)