from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from.models import Vehiculos, Mantenimiento


def vehiculos(request):
    if request.method == 'POST':
        user = request.user  # Usuario en sesión
        placas = request.POST.get('placa')
        tipo_vehiculo = request.POST.get('tipo')

        Vehiculos.objects.create(user=user, placas=placas,  tipo_vehiculo=tipo_vehiculo)
        return redirect('vehiculos')
    
    vehiculos_list = Vehiculos.objects.filter(user=request.user)  # Mostrar solo los vehículos del usuario en sesión
    return render(request, 'vehiculos.html', {'vehiculos_list': vehiculos_list})


def mantenimientoVehiculos(request, vehiculo_id):
    vehiculo = Vehiculos.objects.get(id=vehiculo_id, user=request.user)  # Asegurarse que el vehículo pertenezca al usuario
    if request.method == 'POST':
        estado = request.POST.get('estado') == 'on'
        descripcion = request.POST.get('descripcion')

        Mantenimiento.objects.create(vehiculo=vehiculo, estado=estado, descripcion=descripcion)
        return redirect('mantenimientoVehiculos', vehiculo_id=vehiculo.id)
    
    estados = Mantenimiento.objects.all
    return render(request, 'estados.html', {'estados': estados, 'vehiculo': vehiculo})



