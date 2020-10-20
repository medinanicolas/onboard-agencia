from django.urls import path
from . import views
 
#Añadir todos los links del website aquí
app_name = "onboardwebsite"
urlpatterns = [
    path('', views.index, name='index'),
]
