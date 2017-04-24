from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Obra(models.Model):
	usuario = models.ForeignKey(User)
	nomeObra = models.CharField(max_length=50)
	sinopse = models.CharField(max_length=500)
	ativada = models.BooleanField()
	capa = models.ImageField(upload_to='obra_capas/', default = 'obra_capas/None/no-img.jpg')
	def __str__(self):
		return self.nomeObra