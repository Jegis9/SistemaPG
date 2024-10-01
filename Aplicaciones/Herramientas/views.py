from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Herramienta, EstadoHerramienta, MantenimientoHerramienta
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.contrib import messages
# Create your views here.


def herramienta(request):
    if request.method == 'POST':
        herramienta_id = request.POST.get('herramienta')
        descripcion = request.POST.get('descripcion')
        tiempo_mantenimiento = request.POST.get('tiempo_mantenimiento')

        if herramienta_id and descripcion and tiempo_mantenimiento:
            herramienta = Herramienta.objects.get(codigo=herramienta_id)
            MantenimientoHerramienta.objects.create(
                herramienta=herramienta,
                descripcion=descripcion,
                tiempo_mantenimiento=tiempo_mantenimiento
            )

        # Si se quiere agregar una nueva herramienta
        nuevo_herramienta = request.POST.get('nuevo_herramienta')
        if nuevo_herramienta:
            Herramienta.objects.create(nombre=nuevo_herramienta)

        return redirect('herramientas')

    else:
        herramientas = Herramienta.objects.all()
        mantenimientos = MantenimientoHerramienta.objects.all()
        return render(request, 'herramientasS.html', {
            "herramientas": herramientas,
            "mantenimientos": mantenimientos,
        })


def estadoHerramienta(request, herramienta_id):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        estado = request.POST.get('estado')
        
        herramienta = Herramienta.objects.get(codigo=herramienta_id)  # Asegúrate de que 'asignado_id' sea un id correcto

        if descripcion and estado:
            EstadoHerramienta.objects.create(
                herramienta=herramienta,
                descripcion=descripcion,
                estado=estado
            )

        return redirect('lEHerramientas')
    else:
        return render(request, 'herramientasEstado.html')




def marcar_arreglado(request, codigo):
    estado = get_object_or_404(EstadoHerramienta, codigo=codigo)
    estado.estado = "Bueno"  # Cambia el estado a "arreglado"
    estado.save()
    messages.success(request, "La herramienta ha sido marcada como arreglada.")
    return redirect('lEHerramientas')  # Redirige de nuevo a la lista


def lEHerramientas(request):
    estados = EstadoHerramienta.objects.filter(estado__in=["malo", "Malo"])  # Filtrar solo los estados no arreglados
    return render(request, 'lHerramientas.html', {"estados": estados})
