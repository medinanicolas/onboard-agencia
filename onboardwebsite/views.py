from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import *
from .models import Header, Nosotros, Post
from django.contrib import messages

#               GENERAL
def index(request):
    header = Header.objects.all()
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
#            POSTS
def post_agregar(request):
    data = {
        "form":PostForm()
    }
    if request.method == "POST":
        formulario=PostForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Post agregado correctamente")
            return redirect(to="onboardwebsite:index")
        else:
            data["form"] = formulario
    return render(request, 'onboardwebsite/posts/agregar.html', data)
#               ADMIN PORTADA
def agregar_header(request):
    data = {"form":HeaderForm()}
    if request.method=="POST":
        formulario = HeaderForm(data=request.POST)
        if Header.objects.all().count() < 1:
            if formulario.is_valid():
                formulario.instance.header_autor = request.user.username
                formulario.save()
                messages.success(request, "Header agregado correctamente")
                return redirect(to="onboardwebsite:portada")
            else:
                data["form"]=formulario
        else:
            messages.error(request, "Ya existe un Header activo")
            return redirect(to="onboardwebsite:portada")
    return render(request, 'onboardwebsite/portada/agregar_header.html', data)
def portada(request):
    header = Header.objects.all()
    nosotros = Nosotros.objects.all()
    data = {"header":header, "nosotros":nosotros}
    if request.user.is_authenticated:
        return render(request, 'onboardwebsite/portada/portada.html', data)
    else:
        messages.error(request, "No tienes permiso para esto")
def agregar_nosotros(request):
    data = {"form":HeaderForm()}
    if request.method=="POST":
        formulario = NosotrosForm(data=request.POST)
        if Nosotros.objects.all().count() < 1:
            if formulario.is_valid():
                formulario.instance.nosotros_autor = request.user.username
                formulario.save()
                messages.success(request, "Nosotros agregado correctamente")
                return redirect(to="onboardwebsite:portada")
            else:
                data["form"]=formulario
        else:
            messages.error(request, "Ya existe un Header activo")
            return redirect(to="onboardwebsite:portada")
    return render(request, 'onboardwebsite/portada/agregar_header.html', data)
