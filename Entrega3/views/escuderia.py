from django.views.generic import ListView # Importamos ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from Entrega3.models import Escuderia


class EscuderiaListView(ListView):
    """
    Vista para listar todos los escuderias.
    """
    model = Escuderia
    template_name = 'Entrega3/escuderias/escuderias_list.html'
    #paginate_by = 10                # Paginación: 10 escuderias por página
    #ordering = ['camada',]  # Ordenar por camada (descendente) y luego por nombre (ascendente)


class EscuderiaDetailView(DetailView):
    """
    Vista para mostrar los detalles de un escuderias específico.
    """
    model = Escuderia
    template_name = 'Entrega3/escuderias/escuderias_detail.html'

class EscuderiaCreateView(CreateView):
    """
    Vista para crear un nuevo escuderias.
    """
    model = Escuderia
    fields = ['nombre', 'TeamPrincipal', 'puesto']
    template_name = 'Entrega3/escuderias/escuderias_form.html'
    success_url = '/escuderias/'  # Redirige a la lista de escuderias después de crear uno nuevo
    

class EscuderiaUpdateView(UpdateView):
    """
    Vista para actualizar un escuderias existente.
    """
    model = Escuderia
    fields = ['nombre', 'TeamPrincipal', 'puesto']
    template_name = 'Entrega3/escuderias/escuderias_form.html'
    success_url = '/escuderias/' 


class EscuderiaDeleteView(DeleteView):
    """
    Vista para eliminar un escuderias existente.
    """
    model = Escuderia
    template_name = 'Entrega3/escuderias/escuderias_confirm_delete.html'
    success_url = '/escuderias/'