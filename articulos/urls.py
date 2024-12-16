from django.urls import path
from .views import (
    VistaListaArticulos,
    VistaInicio,
    VistaDetalleArticulo,
    VistaEdicionArticulo,
    VistaEliminacionArticulo,
    VistaCreacionArticulo,   
)

urlpatterns = [
    path('', VistaInicio.as_view(), name='inicio'),
    path('', VistaListaArticulos.as_view(), name='lista_articulos'),
    path('<int:pk>/', VistaDetalleArticulo.as_view(), name='detalle_articulo'),
    path('<int:pk>/editar/', VistaEdicionArticulo.as_view(), name='edicion_articulo'),
    path('<int:pk>/eliminar/', VistaEliminacionArticulo.as_view(), name='eliminacion_articulo'),
    path('nuevo/', VistaCreacionArticulo.as_view(), name='nuevo_articulo'),
]
