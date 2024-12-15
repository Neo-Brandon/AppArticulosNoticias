from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from .models import Articulo
from .forms import FormularioComentario

# Vista para listar los artículos
class VistaListaArticulos(LoginRequiredMixin, ListView):
    model = Articulo
    template_name = 'lista_articulos.html'
    context_object_name = 'articulos'

# Vista para detalle del artículo y agregar comentarios
class VistaDetalleArticulo(LoginRequiredMixin, FormMixin, DetailView):
    model = Articulo
    template_name = 'detalle_articulo.html'
    context_object_name = 'articulo'
    form_class = FormularioComentario

    def get_success_url(self):
        return reverse('detalle_articulo', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # Obtiene el objeto actual
        form = self.get_form()
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.articulo = self.object
            comentario.usuario = self.request.user
            comentario.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

# Vista para editar un artículo
class VistaEdicionArticulo(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articulo
    fields = ('titulo', 'contenido')
    template_name = 'edicion_articulo.html'

    def test_func(self):
        obj = self.get_object()
        return obj.autor == self.request.user

# Vista para eliminar un artículo
class VistaEliminacionArticulo(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articulo
    template_name = 'eliminacion_articulo.html'
    success_url = reverse_lazy('lista_articulos')

    def test_func(self):
        obj = self.get_object()
        return obj.autor == self.request.user

# Vista para crear un artículo
class VistaCreacionArticulo(LoginRequiredMixin, CreateView):
    model = Articulo
    template_name = 'nuevo_articulo.html'
    fields = ('titulo', 'contenido')
    success_url = reverse_lazy('lista_articulos')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
