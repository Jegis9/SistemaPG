from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ServicioForm, VariosForm, AmbulanciaForm, IncendiosForm
from .models import Servicio
from django.db import transaction

# your_app/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ServicioForm, VariosForm, AmbulanciaForm, IncendiosForm
from .models import Servicio
from django.db import transaction
import logging

logger = logging.getLogger('your_app')  # Asegúrate de usar el nombre correcto de tu aplicación

@transaction.atomic
def agregar_servicio(request):
    if request.method == "POST":
        logger.debug("Petición POST recibida en agregar_servicio.")
        servicio_form = ServicioForm(request.POST)
        tipo_servicio = request.POST.get('servicio')

        # Inicializar solo el formulario específico según el tipo de servicio
        if tipo_servicio == 'Varios':
            varios_form = VariosForm(request.POST)
            ambulancia_form = AmbulanciaForm()
            incendios_form = IncendiosForm()
        elif tipo_servicio == 'Ambulancia':
            ambulancia_form = AmbulanciaForm(request.POST)
            varios_form = VariosForm()
            incendios_form = IncendiosForm()
        elif tipo_servicio == 'Incendios':
            incendios_form = IncendiosForm(request.POST)
            varios_form = VariosForm()
            ambulancia_form = AmbulanciaForm()
        else:
            varios_form = VariosForm()
            ambulancia_form = AmbulanciaForm()
            incendios_form = IncendiosForm()

        # Validar el formulario principal
        if servicio_form.is_valid():
            # Validar el formulario específico si corresponde
            form_especifico_valido = False
            if tipo_servicio == 'Varios':
                form_especifico_valido = varios_form.is_valid()
            elif tipo_servicio == 'Ambulancia':
                form_especifico_valido = ambulancia_form.is_valid()
            elif tipo_servicio == 'Incendios':
                form_especifico_valido = incendios_form.is_valid()
            else:
                form_especifico_valido = True  # Si no hay tipo, no hay formulario específico

            if form_especifico_valido:
                try:
                    with transaction.atomic():
                        servicio = servicio_form.save()

                        if tipo_servicio == 'Varios':
                            varios = varios_form.save(commit=False)
                            varios.servicio = servicio
                            varios.save()
                        elif tipo_servicio == 'Ambulancia':
                            ambulancia = ambulancia_form.save(commit=False)
                            ambulancia.servicio = servicio
                            ambulancia.save()
                        elif tipo_servicio == 'Incendios':
                            incendios = incendios_form.save(commit=False)
                            incendios.servicio = servicio
                            incendios.save()

                    messages.success(request, 'Servicio guardado exitosamente.')
                    return redirect('agregar_servicio')  # Asegúrate de que esta URL esté definida
                except Exception as e:
                    logger.error(f'Error al guardar el servicio: {str(e)}')
                    messages.error(request, f'Error al guardar el servicio: {str(e)}')
            else:
                messages.error(request, 'Por favor, corrija los errores en los campos específicos del servicio.')
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario principal.')

    else:
        servicio_form = ServicioForm()
        varios_form = VariosForm()
        ambulancia_form = AmbulanciaForm()
        incendios_form = IncendiosForm()

    return render(request, 'agregar_servicio.html', {
        'servicio_form': servicio_form,
        'varios_form': varios_form,
        'ambulancia_form': ambulancia_form,
        'incendios_form': incendios_form,
    })




def lista_varios(request):
    # Filtra solo los servicios que están relacionados con el modelo de Varios
    servicios_varios = Servicio.objects.filter(servicio='Varios').select_related('varios')
    return render(request, 'servicios_varios.html', {'servicios_varios': servicios_varios})

def lista_ambulancia(request):
    servicios_ambulancia = Servicio.objects.filter(servicio='Ambulancia').select_related('ambulancia')
    return render(request, 'servicios_ambulancia.html', {'servicios_ambulancia': servicios_ambulancia})

def lista_incendios(request):
    servicios_incendios = Servicio.objects.filter(servicio='Incendios').select_related('incendios')
    return render(request, 'servicios_incendios.html', {'servicios_incendios': servicios_incendios})


def lista_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'lista_servicios.html', {'servicios': servicios})

