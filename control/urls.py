from django.conf.urls import url
from . import views

urlpatterns = [
	#/control/
	url(r'^$', views.index, name='index'),

	#/control/1211/
	url(r'^(?P<numControl>[0-9]+)/$', views.detail, name='detail'),
]