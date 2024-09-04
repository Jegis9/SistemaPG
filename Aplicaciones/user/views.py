from django.shortcuts import render, redirect
# importar libreria para el registro de usuarios
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.

# crear vista para que redirija a index que es la pagina principal
def landingPage(request):
    return render(request, 'index.html')

# crear vista para que redirija a index que es la pagina de registrar usuario
def register(request):
    return render(request, 'register.html')

def logout(request):
    return render(request, 'logout.html')

# crear formulario generado por django para registro de usuarios 
def register(request):
    if request.method == 'POST': # si el metodo es post
        form = CreateUserForm(request.POST) #entonces que cree o reciba los parametros de post
        if form.is_valid(): # si estos son validos entonces
            form.save() # los guarda
            print(f'Usuario guardado: {form}')
            return redirect('/login')
        else: # de lo contrario crea el formulario pero no recibe los datos
            print(f'Errores en el formulario: {form.errors}')
    else:
        form = CreateUserForm()
        print('Error al crear el formulario')
# se crea variable para pasar el formulario
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)
