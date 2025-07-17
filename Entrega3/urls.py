from django.urls import path
from Entrega3.views.other import campeones, index, campeonesForm, escuderiaForm, busquedaPiloto, buscar
from Entrega3.views.pilotos import leerPilotos, pilotoFormulario, eliminarPiloto, editarPiloto
from Entrega3.views.escuderia import EscuderiaCreateView, EscuderiaDeleteView, EscuderiaDetailView, EscuderiaListView, EscuderiaUpdateView

urlpatterns = [
    path('', index, name='index'),
    # path('pilotos/', pilotos, name='pilotos'),
    # path('escuderias/', escuderias, name='escuderias'),
    path('campeones/', campeones, name='campeones'),
    # path('pilotoForm/', pilotoForm, name='pilotoForm'),
    path('campeonesForm/', campeonesForm, name='campeonesForm'),
    path('escuderiaForm/', escuderiaForm, name='escuderiaForm'),
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



]