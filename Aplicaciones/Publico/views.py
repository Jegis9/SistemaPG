from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required #importa libreria para hacer de la pagina requerido el login para poder verla
# Create your views here.

@login_required
def reportEmergency(request):
    return render(request, 'reportEmergency.html')


