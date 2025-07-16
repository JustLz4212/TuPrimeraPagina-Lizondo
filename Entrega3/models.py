from django.db import models

class Piloto(models.Model):
    nombre = models.CharField(max_length=100)  # Campo string de 100 caracteres
    escuderia = models.CharField(max_length=100)
    puntos = models.IntegerField()  # Campo entero

    def __str__(self):
        return f"Nombre: {self.nombre} - Escudería: {self.escuderia} - Puntos: {self.puntos}"

class Escuderia(models.Model):
    nombre = models.CharField(max_length=30)  # Campo string de 30 caracteres
    TeamPrincipal = models.CharField(max_length=30)  # Campo string de 100 caracteres
    puesto = models.IntegerField()  # Campo entero

    def __str__(self):
        return f"Nombre: {self.nombre} - Director: {self.TeamPrincipal} - Puesto: {self.puesto}"

class Campeones(models.Model):
    nombre = models.CharField(max_length=30)  # Campo string de 30 caracteres
    Campeonatos = models.IntegerField()  
    victorias = models.IntegerField() 

    def __str__(self):
        return f"Nombre: {self.nombre} - Campeonatos: {self.Campeonatos} - Victorias: {self.victorias}"
    
