from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required #importa libreria para hacer de la pagina requerido el login para poder verla
from .forms import ProfileForm # importar el formulario donde se encuentra laclase para actualizar y mostrar errores

# Create your views here.

@login_required
def reportEmergency(request):
    return render(request, 'reportEmergency.html')




def profile(request):
    if request.method == 'POST': # si es post (envio)
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)  # entoncves relaciona el usuario con el perfil a realizar el envio
        if form.is_valid(): # si esto es valido
            form.save() # entonces lo guarda
            return redirect('profile')  # y redirije a la pagina de profile (vista html)
    else:
        form = ProfileForm(instance=request.user.profile) # si no es post (get) mostrara el formulario que se desea visualizar
    return render(request, 'profile.html', {'form': form})