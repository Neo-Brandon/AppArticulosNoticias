from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=255)
    contenido =  models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,\
        on_delete=models.CASCADE
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
    