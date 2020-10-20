from django.contrib import admin
#Añadir todos los modelos a los que tendrá acceso el Admin
from .models import Header, Nosotros, Post

admin.site.register(Header)
admin.site.register(Nosotros)
admin.site.register(Post)
