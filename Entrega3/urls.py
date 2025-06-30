from django.urls import path
from .views import campeones, escuderias, pilotos, index

urlpatterns = [
    path('', index, name='index'),
    path('pilotos/', pilotos, name='pilotos'),
    path('escuderias/', escuderias, name='escuderias'),
    path('campeones/', campeones, name='campeones'),
]