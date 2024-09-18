from django.shortcuts import render, redirect
# importar libreria para el registro de usuarios
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
# Create your views here.

# crear vista para que redirija a index que es la pagina principal
def landingPage(request):
    return render(request, 'index.html')

# crear vista para que redirija a index que es la pagina de registrar usuario
def register(request):
    return render(request, 'register.html')

def logout(request):
    return render(request, 'logout.html')




# # crear formulario generado por django para registro de usuarios 
def register(request):
    if request.method == 'POST':# si el metodo es POST (recibe datos)
        form = CreateUserForm(request.POST)#entonces que cree o reciba los parametros de post
        if form.is_valid():# si estos son validos entonces
            user = form.save()# los guarda
            # aqui se manda a llamar al modelo de perfil con su campo relacionado de usuario que se creara
            profile = user.profile
            profile.is_internal = form.cleaned_data.get('is_internal', False) # aqui se define si el perfil del usuario es true o false, debido a que es un usuario externo se dejara en False
            profile.save() # aqui se guarda el perfil del usuario relacionado con el campo is_internal como False
            login(request, user) # aqui se loguea con los datos si todo es correcto
            if profile.is_internal: # verifica si el perfil del usuario que inicia el login es interno is_internal entonces lo redirige a home (en este caaso falso)
                return redirect('home')
            else: # de lo contrario, si el usuario en la variable is_internal es falso entonces que lo redirija a reporEmergency que estara disposible para personas externas a la estacion
                return redirect('reportEmergency')
    else:
        form = CreateUserForm() # si el formulario no es POST (envio de datos) y es GET (carga la pagina)
    
    context = {'form': form} # entonces mostrara el formulario para poder registrarse 
    return render(request, 'register.html', context)

class CustomLoginView(View):    # creamos esta nueva vista para modificar el formulario de login por defecto de django
    def get(self, request): 
        form = AuthenticationForm() # por lo que solicitamos (GET carga la pagina) el formuario de django para autenticacion
        return render(request, 'login.html', {'form': form}) # y lo retornamos en la vista login.html donde se debera de mostrar el formato

    def post(self, request): # si el formulario es (POST envio de datos)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): # verifica si el formulario es valido para poder iniciar sesion
            user = form.get_user() # si el usuario existe (previamente registrado)
            login(request, user)  # se inicia sesión con ese usuario
            # y se obtiene el perfil del usuario autenticado quien hizo la peticion el login
            profile = user.profile  # esto obtiene el perfil relacionado con el usuario

            # Redirige segun el valor de is_internal en el perfil relacionado con el usuario que inicia sesion
            if profile.is_internal:
                return redirect('home')  # Si es is_internal redirige a home (adminsitracion de la estacion)
            else:
                return redirect('reportEmergency')  # Si no es is_internal redirige a reportEmergency (acceso a personas agenas a la estacion)
        return render(request, 'login.html', {'form': form}) # aqui renderiza el formulario dende se cargara el formulario djanfo para el login




def nuevo_registro(request):
    if request.method == 'POST':# si el metodo es POST (recibe datos)
        form = CreateUserForm(request.POST)#entonces que cree o reciba los parametros de post
        if form.is_valid():# si estos son validos entonces
            user = form.save()# los guarda
            # aqui se manda a llamar al modelo de perfil con su campo relacionado de usuario que se creara
            profile = user.profile
            profile.is_internal = True # aqui se define si el perfil del usuario es true o false, debido a que es un usuario externo se dejara en False
            profile.save() # aqui se guarda el perfil del usuario relacionado con el campo is_internal como False
            messages.success(request, 'Nuevo usuario agregado correctamente')
        else:
            print(form.errors)
            
    else:
        form = CreateUserForm() # si el formulario no es POST (envio de datos) y es GET (carga la pagina)


    context = {'formulario': form}
    return render(request, 'registerInternal.html', context)







