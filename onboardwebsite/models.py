from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Header(models.Model):
    titulo_text = models.CharField(max_length=50)
    subtitulo_text = models.CharField(max_length=150)
    pub_date = timezone.now()
    def __str__(self):
        return self.titulo_text
class Nosotros(models.Model):
    nosotros_text = models.CharField(max_length=25)
    descripcion_text = models.TextField(max_length=350)
    nosotros_image = models.ImageField(upload_to='images', default='404.png')
    pub_date = timezone.now()
    def __str__(self):
        return self.nosotros_text
class Post(models.Model):
    promo_text = models.CharField(max_length=25)

    precio_int1 = models.IntegerField()
    post_text1 = models.CharField(max_length=30)
    descripcion_text1 = models.TextField(max_length=175)
    post_image1 = models.ImageField(upload_to='images', default='404.png')

    precio_int2 = models.IntegerField()
    post_text2 = models.CharField(max_length=30)
    descripcion_text2 = models.TextField(max_length=175)
    post_image2 = models.ImageField(upload_to='images', default='404.png')

    precio_int3 = models.IntegerField()
    post_text3 = models.CharField(max_length=30)
    descripcion_text3 = models.TextField(max_length=175)
    post_image3 = models.ImageField(upload_to='images', default='404.png')

    pub_date = timezone.now()
    def __str__(self):
        return self.promo_text
"""class Experiencia(models.Model):
    experiencia_text = models.CharField(max_length=25)
    descripcion_text = models.TextField(max_length=130) 
    Soon: Hacer un modelo de experiencias con usuarios registrados
    Para eso hacer login con sesiones
    """