from django.shortcuts import render, redirect
from django.views import View
from .forms import ServicioForm, VariosForm, AmbulanciaForm, IncendiosForm
from .models import Servicio
from django.urls import reverse
from django.views.generic import ListView
from .models import Servicio, Varios, Ambulancia, Incendios
class ServicioCreateView(View):
    def get(self, request):
        servicio_form = ServicioForm()
        varios_form = VariosForm(prefix='varios')
        ambulancia_form = AmbulanciaForm(prefix='ambulancia')
        incendios_form = IncendiosForm(prefix='incendios')
        return render(request, 'add.html', {
            'servicio_form': servicio_form,
            'varios_form': varios_form,
            'ambulancia_form': ambulancia_form,
            'incendios_form': incendios_form,
        })

    def post(self, request):
        servicio_form = ServicioForm(request.POST)
        varios_form = VariosForm(request.POST, prefix='varios')
        ambulancia_form = AmbulanciaForm(request.POST, prefix='ambulancia')
        incendios_form = IncendiosForm(request.POST, prefix='incendios')
        
        # Obtener el valor del servicio seleccionado
        servicio_choice = request.POST.get('servicio')
        
        if servicio_form.is_valid():
            servicio = servicio_form.save()
            
            if servicio_choice == '1':  # Asumiendo que '1' es para Varios
                if varios_form.is_valid():
                    varios = varios_form.save(commit=False)
                    varios.servicio = servicio
                    varios.save()
            elif servicio_choice == '2':  # Asumiendo que '2' es para Ambulancia
                if ambulancia_form.is_valid():
                    ambulancia = ambulancia_form.save(commit=False)
                    ambulancia.servicio = servicio
                    ambulancia.save()
            elif servicio_choice == '3':  # Asumiendo que '3' es para Incendios
                if incendios_form.is_valid():
                    incendios = incendios_form.save(commit=False)
                    incendios.servicio = servicio
                    incendios.save()
                    
            return redirect(reverse('add'))

        # Si hay errores, renderizar la plantilla nuevamente con los formularios
        return render(request, 'add.html', {
            'servicio_form': servicio_form,
            'varios_form': varios_form,
            'ambulancia_form': ambulancia_form,
            'incendios_form': incendios_form,
        })
        
        
        
        
        
        
class VariosListView(ListView):
    model = Varios
    template_name = 'varios.html'
    context_object_name = 'varios'

class AmbulanciaListView(ListView):
    model = Ambulancia
    template_name = 'ambulancia.html'
    context_object_name = 'ambulancias'

class IncendiosListView(ListView):
    model = Incendios
    template_name = 'incendios.html'
    context_object_name = 'incendios'

# Vista para listar todos los servicios

class ServicioListView(ListView):
    model = Servicio
    template_name = 'servicio_lista.html'
    context_object_name = 'servicios'