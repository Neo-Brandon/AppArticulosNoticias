from django.urls import path
from .views import VistaPaginaInicio, VistaPaginaNosotros

urlpatterns = [
    path('', VistaPaginaInicio.as_view(), name = 'inicio'),
    path('nosotros', VistaPaginaNosotros.as_view(), name='nosotros'),
]