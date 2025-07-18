from django.shortcuts import render
from Entrega3.forms import PilotoFormulario
from Entrega3.models import Piloto
from django.contrib.auth.decorators import login_required

# def leerPilotos(request):
#       pilotos = Piloto.objects.all() 
#       return render(request, "Entrega3/formulario/leerPilotos.html", {"pilotos": pilotos})

# @login_required
# def pilotoFormulario(request):  
#     # Vista para crear un nuevo piloto a través de un formulario

#     if request.method == 'POST':  
#         # Si el usuario envió el formulario (método POST), procesamos los datos

#         miFormulario = PilotoFormulario(request.POST)  
#         # Creamos una instancia del formulario con los datos enviados desde el HTML

#         if miFormulario.is_valid():  
#             # Verificamos que los datos sean válidos (cumplen las reglas del formulario)

#             informacion = miFormulario.cleaned_data  
#             # Accedemos a los datos limpios y validados del formulario (devuelve un diccionario)

#             piloto = Piloto(
#                 nombre=informacion['nombre'],
#                 escuderia=informacion['escuderia'],
#                 puntos=informacion['puntos'],
#             )
#             # Creamos una instancia del modelo Profesor con los datos ingresados

#             piloto.save()  
#             # Guardamos el nuevo profesor en la base de datos

#             return leerPilotos(request)
#             # Redirigimos a la vista que muestra la lista de profesores

#     else:
#         miFormulario = PilotoFormulario()  
#         # Si es una solicitud GET (primera vez que se accede), mostramos el formulario vacío

#     return render(request, "Entrega3/formulario/pilotoFormulario.html", {"miFormulario": miFormulario})  
#     # Renderizamos el formulario en el template HTML, pasando el formulario como contexto

# @login_required
# def eliminarPiloto(request, id_piloto):
 
#     piloto = Piloto.objects.get(id=id_piloto)  # Obtengo el profesor por su ID
#     piloto.delete()
 
#     return leerPilotos(request)
#     # vuelvo al menú

# @login_required
# def editarPiloto(request, id_piloto):
#     piloto = Piloto.objects.get(id=id_piloto)  # Recibe el nombre del piloto que vamos a modificar
#     if request.method == 'POST':
#         miFormulario = PilotoFormulario(request.POST)
#         if miFormulario.is_valid():  # Si pasó la validación de Django
#             informacion = miFormulario.cleaned_data
#             piloto.nombre = informacion['nombre']
#             piloto.escuderia = informacion['escuderia']
#             piloto.puntos = informacion['puntos']
#             piloto.save()
#             return leerPilotos(request)

#     else:
#         miFormulario = PilotoFormulario(
#             initial={
#                 'nombre': piloto.nombre,
#                 'escuderia': piloto.escuderia,
#                 'puntos': piloto.puntos,
#                 }
#         )

#     # Por alguna razón el .id me tira error en VSCode pero funciona todo igual (también lo tiraba con el código de la clase)
#     return render(request, "Entrega3/formulario/editarPiloto.html", {"miFormulario": miFormulario, "piloto_id": piloto.id})

def leerPilotos(request):
    pilotos = Piloto.objects.all() 
    return render(request, "Entrega3/formulario/leerPilotos.html", {"pilotos": pilotos})


@login_required
def pilotoFormulario(request):  
    if request.method == 'POST':  
        miFormulario = PilotoFormulario(request.POST, request.FILES)  # ← Añadir request.FILES

        if miFormulario.is_valid():  
            informacion = miFormulario.cleaned_data

            piloto = Piloto(
                nombre=informacion['nombre'],
                escuderia=informacion['escuderia'],
                puntos=informacion['puntos'],
                fechanac=informacion['fechanac'],            # ← nuevo campo
                image=informacion['image'],                  # ← nuevo campo
            )
            piloto.save()  
            return leerPilotos(request)

    else:
        miFormulario = PilotoFormulario()  

    return render(request, "Entrega3/formulario/pilotoFormulario.html", {"miFormulario": miFormulario})


@login_required
def eliminarPiloto(request, id_piloto):
    piloto = Piloto.objects.get(id=id_piloto)
    piloto.delete()
    return leerPilotos(request)


@login_required
def editarPiloto(request, id_piloto):
    piloto = Piloto.objects.get(id=id_piloto)

    if request.method == 'POST':
        miFormulario = PilotoFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            piloto.nombre = informacion['nombre']
            piloto.escuderia = informacion['escuderia']
            piloto.puntos = informacion['puntos']
            piloto.fechanac = informacion['fechanac']
            if informacion.get('image'):  # ← usa cleaned_data en lugar de request.FILES
                piloto.image = informacion['image']
            piloto.save()
            return leerPilotos(request)

    else:
        miFormulario = PilotoFormulario(initial={
            'nombre': piloto.nombre,
            'escuderia': piloto.escuderia,
            'puntos': piloto.puntos,
            'fechanac': piloto.fechanac.strftime('%Y-%m-%d') if piloto.fechanac else '',
            # image no se setea en initial, porque es archivo
        })

    return render(request, "Entrega3/formulario/editarPiloto.html", {"miFormulario": miFormulario,"piloto_id": piloto.id})
