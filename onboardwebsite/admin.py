from django.contrib import admin
#Añadir todos los modelos a los que tendrá acceso el Admin
from .models import Header, Nosotros, Post, Contacto, Experiencias

admin.site.register(Header)
admin.site.register(Nosotros)
admin.site.register(Post)
admin.site.register(Contacto)
admin.site.register(Experiencias)
