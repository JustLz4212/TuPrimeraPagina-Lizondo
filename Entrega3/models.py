from django.db import models
from django.contrib.auth.models import User


class Piloto(models.Model):
    nombre = models.CharField(max_length=100)
    escuderia = models.CharField(max_length=100)
    puntos = models.IntegerField()
    fechanac = models.DateField(null=True, blank=True)  # Campo opcional
    image = models.ImageField(upload_to='pilotos/', null=True, blank=True)

    def __str__(self):
        return f"Nombre: {self.nombre}"

class Escuderia(models.Model):
    nombre = models.CharField(max_length=30)
    TeamPrincipal = models.CharField(max_length=30)
    puesto = models.IntegerField()
    image = models.ImageField(upload_to='escuderias/', null=True, blank=True)

    def __str__(self):
        return f"Nombre: {self.nombre}"

class Campeones(models.Model):
    nombre = models.CharField(max_length=30)
    campeonatos = models.IntegerField()
    victorias = models.IntegerField()
    image = models.ImageField(upload_to='campeones/', null=True, blank=True)

    def __str__(self):
        return f"Nombre: {self.nombre}"
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
