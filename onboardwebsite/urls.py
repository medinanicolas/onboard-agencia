from django.urls import path
from .views import *
 
#Añadir todos los links del website aquí
app_name = "onboardwebsite"
urlpatterns = [
    path('', index, name='index'),
    path('galeria/', registro, name='galeria'),
    path('reservas/', registro, name='reservas'),
    path('registro/', registro, name='registro'),
    path('contacto/', contacto, name='contacto'),
    path('experiencias/', experiencias, name='experiencias'),
]
