from django.db import models


# Create your models here.

class Banda(models.Model):
	name = models.CharField(max_length=255)
	historia = models.TextField()
	descrip = models.CharField(max_length=150)
	imagen = models.ImageField(blank=True)	
	imagen2 = models.ImageField(blank=True)	
	logo = models.ImageField(blank=True)
	url_video = models.CharField(max_length=255, default="null")
	integrante_1 = models.CharField(max_length=255, default="null")
	integrante_2 = models.CharField(max_length=255, default="null")
	integrante_3 = models.CharField(max_length=255, default="null")
	integrante_4 = models.CharField(max_length=255, default="null")
	integrante_5 = models.CharField(max_length=255, default="null")
	nombre_facebook = models.CharField(max_length=255, default="null")
	url_facebook = models.CharField(max_length=255, default="null")
	nombre_twitter = models.CharField(max_length=255, default="null")
	url_twitter = models.CharField(max_length=255, default="null")
	nombre_youtube = models.CharField(max_length=255, default="null")
	url_youtube = models.CharField(max_length=255, default="null")

	def __str__(self):
		return self.name
	class Meta:
		ordering = ('id',)

class Tomnk(models.Model):
	name = models.CharField(max_length=255)
	reseña = models.TextField(help_text='coloca una reseña de ti' )
	cargo = models.CharField(max_length=255)
	foto = models.ImageField(blank=True)

	def __str__(self):
		return self.name
	
