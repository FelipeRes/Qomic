from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^usuario$', views.usuario),
	url(r'^logout$', views.user_logout),
	url(r'^profile/obra/new/$', views.nova_obra),
	url(r'^profile/obra/(?P<obra_id>[0-9]+)/deletar$', views.deletar_obra),
	url(r'^profile/obra/(?P<obra_id>[0-9]+)/alterar/$', views.alterar_obra),
	url(r'^profile/capitulo/(?P<obra_id>[0-9]+)/new/$', views.novo_capitulo),
	url(r'^profile/capitulo/(?P<capitulo_id>[0-9]+)/alterar/$', views.alterar_capitulo),
	url(r'^profile/capitulo/(?P<capitulo_id>[0-9]+)/deletar$', views.deletar_capitulo),
	url(r'^profile/pagina/(?P<capitulo_id>[0-9]+)/new/$', views.inserir_pagina),
	url(r'^profile/pagina/(?P<pagina_id>[0-9]+)/deletar/$', views.deletar_pagina),
	url(r'^profile$', views.profile),

    url(r'^$', views.index),
]