from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from Entrega3.forms import UserRegisterForm, EditProfileForm#, AvatarForm
# from Entrega3.models import Avatar

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

        return redirect('index')

    form = AuthenticationForm()

    return render(request, "Entrega3/usuario/login.html", {"form": form})

def register(request):

      if request.method == 'POST':

            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"Entrega3/index.html" ,  {"mensaje":"Usuario Creado :)"})

      else:      
            form = UserRegisterForm()     

      return render(request,"Entrega3/usuario/registro.html" ,  {"form":form})


@login_required # con este decorador exigimos que el usuario esté logueado para utilizar esta view
def editarPerfil(request):
    usuario = request.user
    
    if usuario.is_staff == True:
         print("El usuario está activo")

    if request.method == 'POST':

        miFormulario = EditProfileForm(request.POST, instance=usuario)

        if miFormulario.is_valid():

            miFormulario.save()

            return redirect('index')

    else:

        miFormulario = EditProfileForm(instance=usuario)

    return render(request, "Entrega3/usuario/editarPerfil.html", {"form": miFormulario, "usuario": usuario})


# @login_required
# def upload_avatar(request):
#     avatar = Avatar.objects.filter(user=request.user.id).first()
#     if request.method == 'POST':
#         form = AvatarForm(request.POST, request.FILES, instance=avatar)
#         if form.is_valid():
#             form.save()
#             return redirect('inicio')
#     else:
#         form = AvatarForm(instance=avatar)
#     return render(request, 'Entrega3/usuario/upload_avatar.html', {'form': form})