from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Header(models.Model):
    header_title = models.CharField(max_length=50)
    header_text = models.CharField(max_length=150)
    header_pubdate = timezone.now()
    def __str__(self):
        return self.header_title
class Nosotros(models.Model):
    nosotros_text = models.CharField(max_length=25)
    descripcion_text = models.TextField(max_length=350)
    nosotros_image = models.ImageField(upload_to='images', default='404.png')
    pub_date = timezone.now()
    def __str__(self):
        return self.nosotros_text
class Post(models.Model):
    post_precio = models.IntegerField()
    post_text = models.CharField(max_length=30)
    post_descripcion = models.TextField(max_length=175)
    post_image = models.ImageField(upload_to='images', default='404.png')
    pub_date = timezone.now()

    def __str__(self):
        return self.post_text

opciones_consultas = [
    [0,"Consulta"],
    [1,"Reclamo"],
    [2,"Sugerencia"],
    [3,"Felicitaciones"]
]
class Contacto(models.Model):
    nombre = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    tipo_consulta = models.IntegerField(choices=opciones_consultas,default=0)
    mensaje = models.TextField(max_length=350)
    pub_date = timezone.now()
    def __str__(self):
        return self.nombre

opciones_estrellas = [
    [0,"⭐⭐⭐⭐⭐"],
    [1,"⭐⭐⭐⭐"],
    [2,"⭐⭐⭐"],
    [3,"⭐⭐"],
    [4,"⭐"]
]
class Experiencias(models.Model):
    username = models.CharField(max_length=25)
    titulo = models.CharField(max_length=10, help_text="Describe tu experiencia en una palabra")
    calificacion = models.IntegerField(choices=opciones_estrellas)
    mensaje = models.TextField(max_length=350, help_text="Describenos tu experiencia con nuestros servicios")
    pub_date = timezone.now()
    def __str__(self):
        return self.titulo