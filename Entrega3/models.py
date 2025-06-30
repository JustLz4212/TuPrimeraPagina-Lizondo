from django.db import models

class Piloto(models.Model):
    nombre = models.CharField(max_length=100)  # Campo string de 100 caracteres
    # escuderia = models.CharField(max_length=100)
    Puntos = models.IntegerField()  # Campo entero

class Escuderia(models.Model):
    nombre = models.CharField(max_length=30)  # Campo string de 30 caracteres
    TeamPrincipal = models.CharField(max_length=30)  # Campo string de 100 caracteres
    puesto = models.IntegerField()  # Campo entero

class Campeones(models.Model):
    nombre = models.CharField(max_length=30)  # Campo string de 30 caracteres
    Campeonatos = models.IntegerField()  
    victorias = models.IntegerField()  
    
