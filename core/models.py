from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Obra(models.Model):
	def content_obra(instance, filename):
		return '/'.join(['obra_capas', instance.usuario.username, filename])
	usuario = models.ForeignKey(User)
	nomeObra = models.CharField(max_length=50)
	sinopse = models.CharField(max_length=500)
	ativada = models.BooleanField()
	capa = models.ImageField(upload_to=content_obra, default = 'obra_capas/None/no-img.jpg')
	def __str__(self):
		return self.nomeObra

class Capitulo(models.Model):
	def content_capitulo(instance, filename):
		return '/'.join(['capitulo_capas', instance.obra.usuario.username, filename])
	obra = models.ForeignKey(Obra)
	nomeCapitulo = models.CharField(max_length=50)
	disponivel = models.BooleanField()
	capa = models.ImageField(upload_to=content_capitulo, default = 'capitulo_capas/None/no-img.jpg')
	def __str__(self):
		return self.nomeCapitulo

class Pagina(models.Model):
	def content_pagina(instance, filename):
		return '/'.join(['paginas', instance.capitulo.obra.usuario.username, filename])
	capitulo = models.ForeignKey(Capitulo)
	pagina = models.ImageField(upload_to=content_pagina, default = 'paginas/None/no-img.jpg')
	def __str__(self):
		return self.pagina




