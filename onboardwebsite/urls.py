from django.urls import path,include
from .views import *
 
#Añadir todos los links del website aquí
app_name = "onboardwebsite"
urlpatterns = [
    #GENERAL
    path('', index, name='index'),
    path('galeria/', galeria, name='galeria'),
    path('reservas/', registro, name='reservas'),
    path('registro/', registro, name='registro'),
    path('contacto/', contacto, name='contacto'),
    path('experiencias/', experiencias, name='experiencias'),
    #ADMIN
    #   ADMIN PORTADA
    path('portada/', portada, name="portada"),
    path('agregar-header/', agregar_header, name="agregar_header"),
    path('modificar-header/<id>/', modificar_header, name="modificar_header"),
    path('agregar-nosotros', agregar_nosotros, name="agregar_nosotros"),
    path('modificar-nosotros/<id>/', modificar_nosotros, name="modificar_nosotros"),
    
    #   ADMIN POSTS
    path('posts/', posts, name="posts"),
    path('agregar-post/', agregar_post, name="agregar_post"),
    path('modificar-post/<id>/', modificar_post, name="modificar_post"),
    path('eliminar-post/<id>/', eliminar_post, name="eliminar_post"),
    #   ADMIN CONTACTOS
    path('contactos/', contactos, name="contactos"),
    path('', include('pwa.urls')),
]   
