from django.urls import path
from Entrega3.views.other import campeones, escuderias, index, campeonesForm, escuderiaForm, busquedaPiloto, buscar
from Entrega3.views.pilotos import leerPilotos, pilotoFormulario, eliminarPiloto, editarPiloto

urlpatterns = [
    path('', index, name='index'),
    # path('pilotos/', pilotos, name='pilotos'),
    path('escuderias/', escuderias, name='escuderias'),
    path('campeones/', campeones, name='campeones'),
    # path('pilotoForm/', pilotoForm, name='pilotoForm'),
    path('campeonesForm/', campeonesForm, name='campeonesForm'),
    path('escuderiaForm/', escuderiaForm, name='escuderiaForm'),
    path('busquedaPiloto/', busquedaPiloto, name="busquedaPiloto"),
    path('buscar/', buscar, name='buscar'),

    path('pilotos/', leerPilotos, name='pilotos'),
    path('pilotoFormulario/', pilotoFormulario, name='pilotoFormulario'),
    path('eliminarPiloto/<int:id_piloto>/', eliminarPiloto, name='eliminarPiloto'),
    path('editarPiloto/<int:id_piloto>/', editarPiloto, name='editarPiloto'),
]