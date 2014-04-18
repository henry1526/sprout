"""
This is your project's master URL configuration, it defines the set of "root" URLs for the entire project
"""
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = patterns(
    'apps.public.views',
    url(r'^api/users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user-detail'),
    url(r'^api/user$', 'logout'),

    # url(r'^addresses$', AddressList.as_view(), name='address-list'),
    # url(r'^addresses/(?P<pk>[0-9]+)$', AddressDetail.as_view(), name='address-detail'),
    url(r'^users$', UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)$', UserDetail.as_view(), name='user-detail'),
)

urlpatterns += patterns('',
	### This endpoint hooks into the REST Framework. We want to extend functionality,
	### So this is commented out and we have defined our own below
	# url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token')

	url(r'^api-token-auth/', ObtainUserAuthToken.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)