from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #All Auth URLS
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/', direct_to_template, { 'template' : 'profile.html' }),
)