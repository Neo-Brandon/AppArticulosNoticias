from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    categoria = models.ForeignKey(
        'Categoria', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    
    def __str__(self): 
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('detalle_articulo', kwargs={'pk': self.pk})

    
class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=142)
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.comentario
    
    def get_absolute_url(self):
        return reverse('lista_articulos')

