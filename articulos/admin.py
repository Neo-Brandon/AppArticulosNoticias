from django.contrib import admin
from .models import Articulo, Categoria

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha', 'categoria')
    list_filter = ('categoria', 'fecha')
    search_fields = ('titulo', 'contenido')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
