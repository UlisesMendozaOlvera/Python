from django.contrib import admin
from gestorapp.models import Sucursal, TipoSala, Genero, Sala, Pelicula
# Register your models here.
admin.site.register(Sucursal)
admin.site.register(TipoSala)
admin.site.register(Genero)
admin.site.register(Sala)
admin.site.register(Pelicula)