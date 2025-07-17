from django.urls import path
from Entrega3.views.other import campeones, index, campeonesForm, busquedaPiloto, buscar
from Entrega3.views.pilotos import leerPilotos, pilotoFormulario, eliminarPiloto, editarPiloto
from Entrega3.views.escuderia import EscuderiaCreateView, EscuderiaDeleteView, EscuderiaDetailView, EscuderiaListView, EscuderiaUpdateView
from Entrega3.views.campeones import CampeonesCreateView, CampeonesDeleteView, CampeonesDetailView, CampeonesListView, CampeonesUpdateView

urlpatterns = [
    path('', index, name='index'),
    # path('campeones/', campeones, name='campeones'),
    # path('campeonesForm/', campeonesForm, name='campeonesForm'),
    path('busquedaPiloto/', busquedaPiloto, name="busquedaPiloto"),
    path('buscar/', buscar, name='buscar'),

    # CRUD basico
    path('pilotos/', leerPilotos, name='pilotos'),
    path('pilotoFormulario/', pilotoFormulario, name='pilotoFormulario'),
    path('eliminarPiloto/<int:id_piloto>/', eliminarPiloto, name='eliminarPiloto'),
    path('editarPiloto/<int:id_piloto>/', editarPiloto, name='editarPiloto'),

    # Clases basadas en vistas 
    path('escuderias/', EscuderiaListView.as_view(), name='escuderias'), 
    path('escuderias/<int:pk>/', EscuderiaDetailView.as_view(), name='escuderias_detail'),
    path('escuderias/nuevo/', EscuderiaCreateView.as_view(), name='escuderias_new'),
    path('escuderias/editar/<int:pk>/', EscuderiaUpdateView.as_view(), name='escuderias_edit'),
    path('escuderias/borrar/<int:pk>/', EscuderiaDeleteView.as_view(), name='escuderias_delete'),

    # Clases basadas en vistas (copiando de escuderias)
    path('campeones/', CampeonesListView.as_view(), name='campeones'), 
    path('campeones/<int:pk>/', CampeonesDetailView.as_view(), name='campeones_detail'),
    path('campeones/nuevo/', CampeonesCreateView.as_view(), name='campeones_new'),
    path('campeones/editar/<int:pk>/', CampeonesUpdateView.as_view(), name='campeones_edit'),
    path('campeones/borrar/<int:pk>/', CampeonesDeleteView.as_view(), name='campeones_delete'),



]