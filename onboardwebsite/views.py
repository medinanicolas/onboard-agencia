from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import RegistrarUsuario, ContactoUsuario
from .models import Header, Nosotros, Post
from django.contrib import messages
#from django.template import loader

# Configurar todas las vistas del website -> luego agregarlas a urls.py
def index(request):
    header = Header.objects.latest('id')
    nosotros = Nosotros.objects.latest('id')
    post = Post.objects.latest('id')

    context = {'header':header, 'nosotros':nosotros, 'post':post}
    return render(request, 'onboardwebsite/index.html', context)

def contacto(request):
    data = {
        "form" : ContactoUsuario()
    }
    if request.method == "POST":
        formulario = ContactoUsuario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Formulario enviado")
        else:
            data["form"] = formulario
    return render(request, 'onboardwebsite/contacto.html', data)

def registro(request):
    if request.user.is_authenticated:
        messages.error(request, "Ya estás registrado")
        return redirect(to="onboardwebsite:index")
    data = {
        "form":RegistrarUsuario()
    }
    if request.method=="POST":
        formulario = RegistrarUsuario(data=request.POST)
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