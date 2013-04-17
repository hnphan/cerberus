from django.conf.urls import patterns, include, url
from cerberusclient import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^shutdown/', views.shutdown, name='shutdown'),
    url(r'^marketplace/', include('marketplace.urls')),
    url(r'^system/', include('system.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL, 'show_indexes':True}),
)

#urlpatterns += staticfiles_urlpatterns()