from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils.dateparse import parse_date
from .models import Articulo, Categoria
from .forms import FormularioComentario
from django.conf import settings
from django.contrib.auth.decorators import login_required
# Vista para la página principal que muestra los artículos
class VistaInicio(ListView):
    model = Articulo
    template_name = 'inicio.html'  # Plantilla de la página principal
    context_object_name = 'articulos'
    paginate_by = 10  # Paginación: 10 artículos por página

    def get_queryset(self):
        queryset = Articulo.objects.all()
        categoria_id = self.request.GET.get('categoria')
        query = self.request.GET.get('q')
        fecha_inicio = self.request.GET.get('fecha_inicio')
        fecha_fin = self.request.GET.get('fecha_fin')

        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)
        if query:
            queryset = queryset.filter(titulo__icontains=query)
        if fecha_inicio:
            queryset = queryset.filter(fecha_publicacion__gte=parse_date(fecha_inicio))
        if fecha_fin:
            queryset = queryset.filter(fecha_publicacion__lte=parse_date(fecha_fin))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['filtro_categoria'] = self.request.GET.get('categoria', '')
        context['termino_busqueda'] = self.request.GET.get('q', '')
        context['fecha_inicio'] = self.request.GET.get('fecha_inicio', '')
        context['fecha_fin'] = self.request.GET.get('fecha_fin', '')
        return context

# Vista para listar artículos con filtro y paginación
class VistaListaArticulos(ListView):
    model = Articulo
    template_name = 'lista_articulos.html'
    context_object_name = 'articulos'
    paginate_by = 10

    def get_queryset(self):
        queryset = Articulo.objects.all()
        categoria_id = self.request.GET.get('categoria')
        query = self.request.GET.get('q')
        fecha_inicio = self.request.GET.get('fecha_inicio')
        fecha_fin = self.request.GET.get('fecha_fin')

        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)
        if query:
            queryset = queryset.filter(titulo__icontains=query)
        if fecha_inicio:
            queryset = queryset.filter(fecha_publicacion__gte=parse_date(fecha_inicio))
        if fecha_fin:
            queryset = queryset.filter(fecha_publicacion__lte=parse_date(fecha_fin))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['filtro_categoria'] = self.request.GET.get('categoria', '')
        context['termino_busqueda'] = self.request.GET.get('q', '')
        context['fecha_inicio'] = self.request.GET.get('fecha_inicio', '')
        context['fecha_fin'] = self.request.GET.get('fecha_fin', '')
        return context

# Vista para detalle del artículo y agregar comentarios
class VistaDetalleArticulo(FormMixin, DetailView):
    model = Articulo
    template_name = 'detalle_articulo.html'
    context_object_name = 'articulo'
    form_class = FormularioComentario

    def get_success_url(self):
        return reverse('detalle_articulo', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.articulo = self.object
            comentario.usuario = self.request.user
            comentario.save()
            messages.success(request, "¡Comentario agregado con éxito!")
            return redirect(self.get_success_url())
        else:
            messages.error(request, "Hubo un error al agregar el comentario.")
            return self.form_invalid(form)

# Vista para crear un artículo
class VistaCreacionArticulo(LoginRequiredMixin, CreateView):
    model = Articulo
    template_name = 'nuevo_articulo.html'
    fields = ('titulo', 'contenido', 'categoria', 'imagen')
    success_url = reverse_lazy('inicio')  # Redirige a la página principal

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

# Vista para editar un artículo
class VistaEdicionArticulo(LoginRequiredMixin, UpdateView):
    model = Articulo
    fields = ('titulo', 'contenido', 'categoria', 'imagen')
    template_name = 'edicion_articulo.html'

    def test_func(self):
        obj = self.get_object()
        return obj.autor == self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()  # Pasa el formulario al contexto
        return context

# Vista para eliminar un artículo
class VistaEliminacionArticulo(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articulo
    template_name = 'eliminacion_articulo.html'
    success_url = reverse_lazy('inicio')

    def test_func(self):
        obj = self.get_object()
        return obj.autor == self.request.user

# NUEVA VISTA: Página de opciones de suscripción
class VistaOpcionesSuscripcion(TemplateView):
    template_name = 'suscripciones.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar las variables de PayPal al contexto para usarlas en la plantilla
        context['PAYPAL_CLIENT_ID'] = settings.PAYPAL_CLIENT_ID
        context['PAYPAL_MODE'] = settings.PAYPAL_MODE
        return context
    

    
class VistaRegistroCategoria(LoginRequiredMixin, CreateView):
    model = Categoria
    template_name = 'crear_categoria.html'
    success_url = reverse_lazy('lista_articulos')

