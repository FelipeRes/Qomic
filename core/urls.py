from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^usuario$', views.usuario),
	url(r'^logout$', views.user_logout),
	url(r'^profile/obra/(?P<obra_id>[0-9]+)/deletar$', views.deletar_obra),
	url(r'^profile/obra/(?P<obra_id>[0-9]+)/alterar/$', views.alterar_obra),
	url(r'^profile/obra/new/$', views.nova_obra),
	url(r'^profile$', views.profile),
    url(r'^$', views.index),
]