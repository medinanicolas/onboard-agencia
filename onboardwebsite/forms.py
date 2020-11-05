from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Header, Nosotros, Contacto, Experiencias, Post
class HeaderForm(forms.ModelForm):
    class Meta:
        model = Header
        fields = ["header_title", "header_text"]
class NosotrosForm(forms.ModelForm):
    class Meta:
        model = Nosotros
        fields = [
            "nosotros_title",
            "nosotros_text",
            "nosotros_image"
        ]
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
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "post_precio",
            "post_title",
            "post_text",
            "post_image",
        ]