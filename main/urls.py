from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^people$', views.people, name='people'),
	url(r'^awards', views.awards, name='awards'),
	url(r'^research', views.research, name='research'),
	url(r'^about', views.about, name='about'),
]
