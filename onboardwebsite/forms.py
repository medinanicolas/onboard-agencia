from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Contacto, Experiencias

class RegistrarUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
            
class ContactoUsuario(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = "__all__"

class ExperienciasUsuario(forms.ModelForm):
    class Meta:
        model = Experiencias
        fields = [
            "titulo",
            "calificacion",
            "mensaje",
        ]
