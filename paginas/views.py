from django.views.generic import TemplateView
from datetime import datetime

# Create your views here.
class VistaPaginaInicio(TemplateView):
    template_name = 'inicio.html'
    
    def get_context_data(self, **kwargs):
        # Obtén el contexto de la clase base
        context = super().get_context_data(**kwargs)
        
        # Añadir la fecha y hora actual al contexto
        fecha_hora_actual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')  # Formato Día/Mes/Año HH:MM:SS
        context['fecha_hora_actual'] = fecha_hora_actual
        
        return context
    
class VistaPaginaNosotros(TemplateView):
    template_name = 'nosotros.html'
    
    
    
    
