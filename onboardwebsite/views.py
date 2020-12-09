from django.shortcuts import render, HttpResponse,redirect,get_object_or_404, Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from .forms import HeaderForm, NosotrosForm, RegistrarUsuario, ContactoUsuario, ExperienciasUsuario, PostForm
from .models import Header, Nosotros, Post, Experiencias, Contacto
from django.contrib import messages
from django.core.paginator import Paginator
from rest_framework import viewsets
from .serializers import PostSerializer
#               GENERAL
def index(request):
    header = Header.objects.latest('id')
    nosotros = Nosotros.objects.latest('id')
    posts = Post.objects.order_by('-id')[:3]
    experiencias = Experiencias.objects.all()
    data = {'header':header, 'nosotros':nosotros, "posts":posts, "experiencias":experiencias}
    return render(request, 'onboardwebsite/index.html', data)
def registro(request):
    if request.user.is_authenticated:
        messages.warning(request, "Ya estás registrado")
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
@login_required
def experiencias(request):
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
#            ADMIN POSTS
@permission_required("onboardwebsite.view_post")
def posts(request):
    posts = Post.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(posts, 3)
        posts = paginator.page(page)
    except Exception as e:
        raise Http404
    data= {"entity":posts, "paginator":paginator}
    return render(request, "onboardwebsite/admin/posts/posts.html", data)
@permission_required("onboardwebsite.add_post")
def agregar_post(request):
    data = {
        "form":PostForm()
    }
    if request.method == "POST":
        formulario=PostForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.instance.post_autor = request.user.username
            formulario.save()
            messages.success(request, "Post agregado correctamente")
            return redirect(to="onboardwebsite:posts")
        else:
            data["form"] = formulario
    return render(request, 'onboardwebsite/admin/posts/agregar.html', data)
@permission_required("onboardwebsite.change_post")
def modificar_post(request, id):
    post = get_object_or_404(Post, id=id)
    data = {"form":PostForm(instance=post)}
    if request.method=="POST":
        formulario = PostForm(data=request.POST, files=request.FILES, instance=post)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Post actualizado correctamente")
            return redirect(to="onboardwebsite:posts")
        else:
            data["form"]=formulario
    return render(request, 'onboardwebsite/admin/posts/modificar.html', data)
@permission_required("onboardwebsite.delete_post")
def eliminar_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, "Post eliminado")
    return redirect(to="onboardwebsite:posts")
#               ADMIN PORTADA
@permission_required("onboardwebsite.view_header")
@permission_required("onboardwebsite.view_nosotros")
def portada(request):
    header = Header.objects.all()
    nosotros = Nosotros.objects.all()
    data = {"header":header, "nosotros":nosotros}
    return render(request, 'onboardwebsite/admin/portada/portada.html', data)
@permission_required("onboardwebsite.add_header")
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
            messages.warning(request, "Ya existe un Header activo")
            return redirect(to="onboardwebsite:portada")
    return render(request, 'onboardwebsite/admin/portada/agregar_header.html', data)
@permission_required("onboardwebsite.change_header")
def modificar_header(request, id):
    header = get_object_or_404(Header, id=id)
    data = {"form":HeaderForm(instance=header)}
    if request.method=="POST":
        formulario = HeaderForm(data=request.POST, files=request.FILES, instance=header)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Header actualizado correctamente")
            return redirect(to="onboardwebsite:portada")
        else:
            data["form"]=formulario
    return render(request, 'onboardwebsite/admin/portada/modificar_header.html', data)
@permission_required("onboardwebsite.add_nosotros")
def agregar_nosotros(request):
    data = {"form":NosotrosForm()}
    if request.method=="POST":
        formulario = NosotrosForm(data=request.POST, files=request.POST)
        if Nosotros.objects.all().count() < 1:
            if formulario.is_valid():
                formulario.instance.nosotros_autor = request.user.username
                formulario.save()
                messages.success(request, "Nosotros agregado correctamente")
                return redirect(to="onboardwebsite:portada")
            else:
                data["form"]=formulario
        else:
            messages.warning(request, "Ya existe un Nosotros activo")
            return redirect(to="onboardwebsite:portada")
    return render(request, 'onboardwebsite/admin/portada/agregar_nosotros.html', data)
@permission_required("onboardwebsite.change_nosotros")
def modificar_nosotros(request, id):
    nosotros = get_object_or_404(Nosotros, id=id)
    data = {"form":NosotrosForm(instance=nosotros)}
    if request.method=="POST":
        formulario = NosotrosForm(data=request.POST, files=request.FILES, instance=nosotros)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Nosotros actualizado correctamente")
            return redirect(to="onboardwebsite:portada")
        else:
            data["form"]=formulario
    return render(request, 'onboardwebsite/admin/portada/modificar_nosotros.html', data)
@permission_required("onboardwebsite.view_contacto")
def contactos(request):
    contactos = Contacto.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(contactos, 10)
        contactos = paginator.page(page)
    except Exception as e:
        raise Http404
    data= {"entity":contactos, "paginator":paginator}
    return render(request, 'onboardwebsite/admin/contactos.html', data)
#Cambiar 
def galeria(request):
    posts = Post.objects.all()
    data = {
        'lugares': posts
    }
    return render(request, "onboardwebsite/galeria.html",data)
class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        post = Post.objects.all()
        post_title = self.request.GET.get('titulo')
        if post_title:
            post = post.filter(post_title__contains=post_title)
        return post