from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	url(r'^$', views.memory, name='memory'),
	url(r'^(?P<title>.+)/$', views.detail, name='memory detail'),
] 