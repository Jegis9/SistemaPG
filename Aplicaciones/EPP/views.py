from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Epp, PersonalEpps, EstadoEPP
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
# Create your views here.


def epp(request):
    if request.method == 'POST':
        personal_id = request.POST.get('personal')
        epp_id = request.POST.get('epp')

        if personal_id and epp_id:
            # Obtén las instancias de User y Epp para guardarlas en el modelo de relación
            personal = User.objects.get(id=personal_id)
            epp = Epp.objects.get(codigo=epp_id)

            # Crear la asignación de EPP al personal
            PersonalEpps.objects.create(idPersonal=personal, idEpp=epp)

        # Si se quiere agregar un nuevo EPP
        nuevo_epp = request.POST.get('nuevo_epp')
        if nuevo_epp:
            Epp.objects.create(nombre=nuevo_epp)

        return redirect('epp')  # Redireccionar después de guardar

    else:
        users = User.objects.filter(profile__is_internal=True)
        epps = Epp.objects.all()
        asignaciones = PersonalEpps.objects.all()
        return render(request, 'epp.html', {
            "users": users, 
            "epps": epps, 
            "asignaciones": asignaciones
        })




def estadoEPP(request, asignado_id):
    # Obtener la instancia de PersonalEpps
    asignacion = get_object_or_404(PersonalEpps, id=asignado_id)
    
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        if descripcion:
            # Crear un nuevo estado para el EPP
            EstadoEPP.objects.create(PersonalEpps=asignacion,descripcion=descripcion, reportado=timezone.now())

        return redirect('epp')  # Redirigir a la página principal después de guardar
    else:
        # Si el método es GET, mostrar el modal
        return render(request, 'epp.html', {"asignacion": asignacion})  # Cargar la página con la asignación


def lEpp(request):
    
    estados = EstadoEPP.objects.all()
    
    return render(request, 'lepp.html', {"estados": estados})



