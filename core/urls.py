from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^usuario$', views.usuario),
    url(r'^$', views.index),
]