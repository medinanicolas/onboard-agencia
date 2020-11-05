from django.urls import path
from .views import *
 
#Añadir todos los links del website aquí
app_name = "onboardwebsite"
urlpatterns = [
    #GENERAL
    path('', index, name='index'),
    path('galeria/', registro, name='galeria'),
    path('reservas/', registro, name='reservas'),
    path('registro/', registro, name='registro'),
    path('contacto/', contacto, name='contacto'),
    path('experiencias/', experiencias, name='experiencias'),
    #ADMIN PORTADA
    path('portada/', portada, name="portada"),
    path('agregar_header/', agregar_header, name="agregar_portada"),
    #ADMIN POSTS
    path('agregar_post/', post_agregar, name="post_agregar")
]   
