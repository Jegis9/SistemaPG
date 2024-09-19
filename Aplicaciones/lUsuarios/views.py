from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def lUsuarios(request):
    # Obtenemos la lista de todos los usuarios registrados
  
    users = User.objects.filter(profile__is_internal=False)
    return render(request, 'listaUsuarios.html', {"object_list": users})


def lInternos(request):
    # Obtenemos la lista de todos los usuarios registrados
  
    users = User.objects.filter(profile__is_internal=True)
    return render(request, 'listaInternos.html', {"object_list": users})
