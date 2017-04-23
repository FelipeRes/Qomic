from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^usuario$', views.usuario),
	url(r'^logout$', views.user_logout),
	url(r'^profile$', views.profile),
	url(r'^profile/nova_obra/$', views.nova_obra),
    url(r'^$', views.index),
]