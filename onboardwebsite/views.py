from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Header, Nosotros, Post
#from django.template import loader

# Configurar todas las vistas del website -> luego agregarlas a urls.py
def index(request):
    header = Header.objects.latest('id')
    nosotros = Nosotros.objects.latest('id')
    post = Post.objects.latest('id')

    context = {'header':header, 'nosotros':nosotros, 'post':post}
    return render(request, 'onboardwebsite/index.html', context)
