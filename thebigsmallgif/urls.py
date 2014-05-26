# example/simple/urls.py

from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
	url(r'^$', views.home),
	url(r'^(?P<slug>[a-zA-Z0-9_.-]+)/$', views.home),
	url(r'^(?P<slug>[a-zA-Z0-9_.-]+)/$', views.home),
	url(r'^(?P<slug>[a-zA-Z0-9_.-]+)/(?P<size>[0-9]+)/$', views.home)
)