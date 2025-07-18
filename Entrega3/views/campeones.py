from django.views.generic import ListView # Importamos ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from Entrega3.models import Campeones, Avatar


class CampeonesListView(ListView):
    """
    Vista para listar todos los campeones.
    """
    model = Campeones
    template_name = 'Entrega3/campeones/campeones_list.html'
    # paginate_by = 10
    # ordering = ['camada']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Agregamos el avatar del usuario al contexto si está logueado
        if self.request.user.is_authenticated:
            context['avatar'] = Avatar.objects.filter(user=self.request.user).first()
        
        return context
    


class CampeonesDetailView(DetailView):
    """
    Vista para mostrar los detalles de un campeones específico.
    """
    model = Campeones
    template_name = 'Entrega3/campeones/campeones_detail.html'

class CampeonesCreateView(CreateView):
    """
    Vista para crear un nuevo campeones.
    """
    model = Campeones
    fields = ['nombre', 'campeonatos', 'victorias']
    template_name = 'Entrega3/campeones/campeones_form.html'
    success_url = '/campeones/'  # Redirige a la lista de campeones después de crear uno nuevo
    

class CampeonesUpdateView(UpdateView):
    """
    Vista para actualizar un campeones existente.
    """
    model = Campeones
    fields = ['nombre', 'campeonatos', 'victorias']
    template_name = 'Entrega3/campeones/campeones_form.html'
    success_url = '/campeones/' 


class CampeonesDeleteView(DeleteView):
    """
    Vista para eliminar un campeon existente.
    """
    model = Campeones
    template_name = 'Entrega3/campeones/campeones_confirm_delete.html'
    success_url = '/campeones/'