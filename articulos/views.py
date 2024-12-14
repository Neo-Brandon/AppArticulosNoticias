from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormView
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.urls import reverse_lazy
from .models import Articulo
from .forms import FormularioComentario
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy, reverse

# Create your views here.

class VistaListaArticulos(LoginRequiredMixin,ListView):
    model = Articulo
    template_name = 'lista_articulos.html'
    
class ComentarioGet(DetailView):
    model = Articulo
    template_name = 'detalle_articulo.html'
    
    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['form'] = FormularioComentario()
      return context

class ComentarioPost(SingleObjectMixin, FormView):
    model = Articulo
    from_class = FormularioComentario
    template_name = 'detalle_articulo.html'
    
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        comentario = form.save(commit=False)
        comentario.articulo = self.object
    
  
class VistaDetalleArticulo(LoginRequiredMixin, DetailView):
  def get(self, request, *args, **kwargs):
      vista = ComentarioGet.as_view()
      return vista(request, *args, **kwargs)
  
  def post(self, request, *args, **kwargs):
      vista = ComentarioPost.as_view()
      return vista(request, *args, **kwargs)
      
class VistaEdicionArticulo(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Articulo
    fields = (
        'titulo',
        'contenido',
    )
    
    template_name = 'edicion_articulo.html'
    
    def test_func(self):
        obj = self.get_object()  # Correcto
        return obj.autor == self.request.user
    
class VistaEliminacionArticulo(LoginRequiredMixin,UserPassesTestMixin,  DeleteView):
    model = Articulo
    template_name = 'eliminacion_articulo.html'
    success_url = reverse_lazy('lista_articulos')
    
    def test_func(self):
        obj = self.get_object()  # Correcto
        return obj.autor == self.request.user
    
class VistaCreacionArticulo(LoginRequiredMixin, CreateView):
    model = Articulo
    template_name = 'nuevo_articulo.html'
    fields = (
        'titulo',
        'contenido',
    )

    def form_valid(self, form):
      form.instance.autor = self.request.user
      return super().form_valid(form)

    