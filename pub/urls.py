from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.pub, name='pub'),
	url(r'book/$', views.book, name='book'),
	url(r'journal/$', views.journal),
	url(r'journal/(?P<title>.*)', views.journal_pdf),
	url(r'conference/$', views.conference, name='conference'),
	url(r'conference/(?P<title>.*)', views.conference_pdf),
	url(r'upload', views.upload, name='upload'),
]