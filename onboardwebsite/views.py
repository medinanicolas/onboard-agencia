from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import RegistrarUsuario, ContactoUsuario, ExperienciasUsuario
from .models import Header, Nosotros, Post
from django.contrib import messages
#from django.template import loader

# Configurar todas las vistas del website -> luego agregarlas a urls.py
def index(request):
    header = Header.objects.latest('id')
    nosotros = Nosotros.objects.latest('id')
    posts = Post.objects.order_by('-id')[:3]
    data = {'header':header, 'nosotros':nosotros, "posts":posts}
    return render(request, 'onboardwebsite/index.html', data)
def registro(request):
    if request.user.is_authenticated:
        messages.error(request, "Ya estás registrado")
        return redirect(to="onboardwebsite:index") 
    data = {
        "form":RegistrarUsuario()
    }
    if request.method=="POST":
        formulario = RegistrarUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="onboardwebsite:index")
        data["form"] = formulario
    else:
        formulario = RegistrarUsuario()
    return render(request, 'registration/registro.html', data)

def contacto(request):
    data = {
        "form" : ContactoUsuario()
    }
    if request.method == "POST":
        formulario = ContactoUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Formulario enviado")
        else:
            data["form"] = formulario
    return render(request, 'onboardwebsite/contacto.html', data)


def experiencias(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes estar registrado para calificarnos")
        return redirect(to="onboardwebsite:index") 
    data = {
        "form":ExperienciasUsuario()
    }
    if request.method=="POST":
        formulario = ExperienciasUsuario(request.POST)
        if formulario.is_valid():
            formulario.instance.username = request.user.username
            formulario.save()
            messages.success(request, "Gracias por calificarnos")
            return redirect(to="onboardwebsite:experiencias")
        data["form"] = formulario
    else:
        formulario = ExperienciasUsuario()
    return render(request, 'onboardwebsite/experiencias.html', data)
