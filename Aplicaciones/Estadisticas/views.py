# Estadisticas/views.py
from django.shortcuts import render
from Aplicaciones.Publico.models import Emergencias
from django.contrib.auth.models import User
from Aplicaciones.Herramientas.models import EstadoHerramienta

def estadisticas(request):
    # Contadores para emergencias
    total_emergencias_atendidas = Emergencias.objects.filter(atendido=True).count()
    total_emergencias_pendientes = Emergencias.objects.filter(atendido=False).count()
    
    # Contadores para usuarios
    total_usuarios_internos = User.objects.filter(profile__is_internal=True).count()
    total_usuarios_externos = User.objects.filter(profile__is_internal=False).count()
    
    # Contadores para herramientas
    total_herramientas_malas = EstadoHerramienta.objects.filter(estado__in=["malo", "Malo"]).count()
    total_herramientas_arregladas = EstadoHerramienta.objects.filter(estado__in=["Bueno", "arreglado"]).count()

    context = {
        'emergencias_atendidas': total_emergencias_atendidas,
        'emergencias_pendientes': total_emergencias_pendientes,
        'usuarios_internos': total_usuarios_internos,
        'usuarios_externos': total_usuarios_externos,
        'herramientas_malas': total_herramientas_malas,
        'herramientas_arregladas': total_herramientas_arregladas,
    }
    
    return render(request, 'estadisticas.html', context)