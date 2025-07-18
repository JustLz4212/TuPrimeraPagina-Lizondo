from django.shortcuts import render
from ..models import Campeones, Piloto, Escuderia, Avatar
from ..forms import PilotoFormulario, CampeonesFormulario, EscuderiaFormulario
from django.http import HttpResponse

# def index(request):
#     return render(request, "Entrega3/index.html")

def index(request):
    avatar = Avatar.objects.filter(user=request.user.id).first()
    return render(request, "Entrega3/index.html", {"avatar": avatar if avatar else None})

def campeones(request):
    return render(request, "Entrega3/Campeones.html")

def escuderias(request):
    return render(request, "Entrega3/Escuderias.html")

def pilotos(request):
    return render(request, "Entrega3/Pilotos.html")


def pilotoForm(request):
      if request.method == "POST":
            miFormulario = PilotoFormulario(request.POST) # Aqui me llega la informacion del html
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  piloto = Piloto(nombre=informacion["nombre"], puntos=informacion["puntos"])
                  piloto.save()
                  return render(request, "Entrega3/Pilotos.html")
      else:
            miFormulario = PilotoFormulario() # Formulario vacio para construir el html
 
      return render(request, "Entrega3/formulario/pilotoFormulario.html", {"miFormulario": miFormulario})

def campeonesForm(request):
      if request.method == "POST":
            miFormulario = CampeonesFormulario(request.POST) # Aqui me llega la informacion del html
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  campeon = Campeones(nombre=informacion["nombre"], Campeonatos=informacion["campeonatos"], victorias=informacion["victorias"])
                  campeon.save()
                  return render(request, "Entrega3/Campeones.html")
      else:
            miFormulario = CampeonesFormulario() # Formulario vacio para construir el html
 
      return render(request, "Entrega3/formulario/campeonesFormulario.html", {"miFormulario": miFormulario})

def escuderiaForm(request):
      if request.method == "POST":
            miFormulario = EscuderiaFormulario(request.POST) # Aqui me llega la informacion del html
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  escuderia = Escuderia(nombre=informacion["nombre"], TeamPrincipal=informacion["teamprincipal"], puesto=informacion["puesto"])
                  escuderia.save()
                  return render(request, "Entrega3/Escuderias.html")
      else:
            miFormulario = EscuderiaFormulario() # Formulario vacio para construir el html
 
      return render(request, "Entrega3/formulario/escuderiaFormulario.html", {"miFormulario": miFormulario})

def busquedaPiloto(request):
    return render(request, "Entrega3/formulario/busquedaPiloto.html")


# def buscar(request):
#     if request.GET["escuderia"]:
#         #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }"
#         escuderia = request.GET['escuderia']
#         # icontains es un filtro que se usa para buscar coincidencias en los campos de texto de la base de datos, 
#         # sin importar si las letras están en mayúsculas o minúsculas
#         pilotos = Piloto.objects.filter(escuderia__icontains=escuderia)

#         return render(request, "Entrega3/formulario/resultadosBusqueda.html", {"pilotos": pilotos, "escuderia": escuderia})

#     else:
#         respuesta = "No enviaste datos"

#         # No olvidar from django.http import HttpResponse
#         return HttpResponse(respuesta)

def buscar(request):
    escuderia = request.GET.get('escuderia', '')
    pilotos = Piloto.objects.filter(escuderia__icontains=escuderia)
    return render(request, "Entrega3/formulario/leerPilotos.html", {"pilotos": pilotos})

def about_me(request):
    avatar = None
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user).first()
    return render(request, "Entrega3/about_me.html", {"avatar": avatar})