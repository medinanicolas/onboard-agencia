from django.urls import path
from . import views
 
#Añadir todos los links del website aquí
app_name = "onboardwebsite"
urlpatterns = [
    path('', views.index, name='index'),
    path('galeria/', views.registro, name='galeria'),
    path('reservas/', views.registro, name='reservas'),
    path('registro/', views.registro, name='registro'),
    path('contacto/', views.contacto, name='contacto'),
    path('experiencias/', views.registro, name='experiencias'),
]
