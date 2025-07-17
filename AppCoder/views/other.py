from django.shortcuts import render
from ..models import Curso, Profesor #Avatar
from ..forms import CursoFormulario, ProfesorFormulario
from django.http import HttpResponse

# def inicio(request):
#     avatar = Avatar.objects.filter(user=request.user.id).first()
#     return render(request, "AppCoder/index.html", {"avatar": avatar if avatar else None})

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def cursoFormulario2(request):
      if request.method == "POST":
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                  curso.save()
                  return render(request, "AppCoder/cursos.html")
      else:
            miFormulario = CursoFormulario() # Formulario vacio para construir el html
 
      return render(request, "AppCoder/formulario/cursoFormulario2.html", {"miFormulario": miFormulario})

def busquedaCamada(request):
    return render(request, "AppCoder/formulario/busquedaCamada.html")


def buscar(request):
    if request.GET["camada"]:
        #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }"
        camada = request.GET['camada']
        # icontains es un filtro que se usa para buscar coincidencias en los campos de texto de la base de datos, 
        # sin importar si las letras están en mayúsculas o minúsculas
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, "AppCoder/formulario/resultadosBusqueda.html", {"cursos": cursos, "camada": camada})

    else:
        respuesta = "No enviaste datos"

        # No olvidar from django.http import HttpResponse
        return HttpResponse(respuesta)
    
def profesorFormulario(request):  
    # Vista para crear un nuevo profesor a través de un formulario

    if request.method == 'POST':  
        # Si el usuario envió el formulario (método POST), procesamos los datos

        miFormulario = ProfesorFormulario(request.POST)  
        # Creamos una instancia del formulario con los datos enviados desde el HTML

        if miFormulario.is_valid():  
            # Verificamos que los datos sean válidos (cumplen las reglas del formulario)

            informacion = miFormulario.cleaned_data  
            # Accedemos a los datos limpios y validados del formulario (devuelve un diccionario)

            profesor = Profesor(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                email=informacion['email'],
                profesion=informacion['profesion']
            )
            # Creamos una instancia del modelo Profesor con los datos ingresados

            profesor.save()  
            # Guardamos el nuevo profesor en la base de datos

            return render(request, "AppCoder/index.html")
            # Redirigimos a la vista que muestra la lista de profesores

    else:
        miFormulario = ProfesorFormulario()  
        # Si es una solicitud GET (primera vez que se accede), mostramos el formulario vacío

    return render(request, "AppCoder/formulario/profesorFormulario.html", {"miFormulario": miFormulario})  
    # Renderizamos el formulario en el template HTML, pasando el formulario como contexto