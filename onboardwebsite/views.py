from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrarUsuario
from .models import Header, Nosotros, Post
#from django.template import loader

# Configurar todas las vistas del website -> luego agregarlas a urls.py
def index(request):
    header = Header.objects.latest('id')
    nosotros = Nosotros.objects.latest('id')
    post = Post.objects.latest('id')

    context = {'header':header, 'nosotros':nosotros, 'post':post}
    return render(request, 'onboardwebsite/index.html', context)

def registro(request):
    if request.method=="POST":
        form = RegistrarUsuario(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegistrarUsuario()
    return render(request, 'onboardwebsite/registro.html', {'form':form})