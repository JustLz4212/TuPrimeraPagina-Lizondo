from django import forms

class PilotoFormulario(forms.Form):
    nombre = forms.CharField()
    escuderia = forms.CharField()
    puntos = forms.IntegerField()

class EscuderiaFormulario(forms.Form):
    nombre = forms.CharField()
    teamprincipal = forms.CharField()
    puesto = forms.IntegerField()

class CampeonesFormulario(forms.Form):
    nombre = forms.CharField()
    campeonatos = forms.IntegerField()
    victorias = forms.IntegerField()
 