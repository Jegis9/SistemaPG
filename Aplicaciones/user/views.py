from django.shortcuts import render, redirect
# importar libreria para el registro de usuarios
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

# crear vista para que redirija a index que es la pagina principal
def landingPage(request):
    return render(request, 'index.html')

# crear vista para que redirija a index que es la pagina de registrar usuario
def register(request):
    return render(request, 'register.html')

# crear vista para que redirija a index que es la pagina de inicio de sesion de usuario
def login(request):
    return render(request, 'login.html')


# crear formulario generado por django para registro de usuarios 
def register(request):
    if request.method == 'POST': # si el metodo es post
        form = UserCreationForm(request.POST) #entonces que cree o reciba los parametros de post
        if form.is_valid(): # si estos son validos entonces
            form.save() # los guarda
            print(f'Usuario guardado: {form}')
            return redirect('login')
    else:
        form = UserCreationForm() # de lo contrario crea el formulario pero no recibe los datos
        

    # se crea variable para pasar el formulario
    context = {
        'form':form
    }
    return render(request, 'register.html', context)