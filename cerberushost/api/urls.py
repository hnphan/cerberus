from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from django.conf.urls import include

urlpatterns = patterns('api.views',
	url(r'^$', 'api_root'),
    url(r'^packages/$', views.PackageList.as_view(), name="package-list"),
    url(r'^packages/(?P<pk>[0-9]+)/$', views.PackageDetail.as_view(), name="package-detail"),
    url(r'^users/$', views.UserList.as_view(), name="user-list"),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserInstance.as_view(), name="user-detail"),
)

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)
