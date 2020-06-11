from django.conf.urls import url
from .views import *
from django.views import View

urlpatterns = [
	url(r'^$', index, name = 'index'),
	url(r'^displayClients$', displayClients, name = 'displayClients'),
	url(r'^search$', search, name = 'search'),
	url(r'^addClient$', addClient, name='addClient'),
	url(r'^editClient/(?P<pk>\d+)$', editClient, name='editClient')
]