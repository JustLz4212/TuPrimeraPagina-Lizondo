from django.views.generic import ListView # Importamos ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from Entrega3.models import Escuderia, Avatar

class EscuderiaListView(ListView):
    """
    Vista para listar todas las escuderías.
    """
    model = Escuderia
    template_name = 'Entrega3/escuderias/escuderias_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Agregamos el avatar del usuario al contexto si está autenticado
        if self.request.user.is_authenticated:
            context['avatar'] = Avatar.objects.filter(user=self.request.user).first()
        
        return context



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