from django.contrib import admin
from .models import Articulo, Categoria

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'categoria')
    list_filter = ('categoria', 'fecha_publicacion')
    search_fields = ('titulo', 'contenido')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
