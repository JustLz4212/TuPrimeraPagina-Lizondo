from django.urls import path
from .views import campeones, escuderias, pilotos, index, pilotoForm, campeonesForm, escuderiaForm

urlpatterns = [
    path('', index, name='index'),
    path('pilotos/', pilotos, name='pilotos'),
    path('escuderias/', escuderias, name='escuderias'),
    path('campeones/', campeones, name='campeones'),
    path('pilotoForm/', pilotoForm, name='pilotoForm'),
    path('campeonesForm/', campeonesForm, name='campeonesForm'),
    path('escuderiaForm/', escuderiaForm, name='escuderiaForm'),
]