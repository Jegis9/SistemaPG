from django.shortcuts import render, redirect
from .models import Insumos, InsumoLog
# Create your views here.

def home(request):
    insumosList = Insumos.objects.all()
    return render(request, "insumos.html", {"insumos": insumosList})




def registrarInsumo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        stock_inicial = request.POST.get('cantidadInicial')
     

        Insumos.objects.create(nombre=nombre, stock_inicial=stock_inicial, stock_actual=stock_inicial)

        return redirect('/')
    else:
        return redirect('/')
    
    
def eliminacionInsumo(request, codigo):
    insumo = Insumos.objects.get(codigo=codigo)
    insumo.delete()
    
    return redirect('/')







def edicionInsumo(request, codigo):
    insumo = Insumos.objects.get(codigo=codigo)
    return render(request, "insumosEditar.html", {"insumo": insumo})


def editarInsumo(request):
    codigo = request.POST.get('codigo')
    nombre = request.POST.get('nombre')
    stock_inicial = int(request.POST.get('cantidadInicial'))
    stock_actual = int(request.POST.get('cantidadActual'))
    cantidadTomada = int(request.POST.get('cantidadTomada'))
    
    if stock_actual >= cantidadTomada:
        stock_actual = stock_actual-cantidadTomada
            
        insumo = Insumos.objects.get(codigo = codigo)
        insumo.nombre = nombre
        insumo.stock_inicial = stock_inicial
        insumo.stock_actual = stock_actual
    
        insumo.save()
        
                # Crear un log del descuento
        InsumoLog.objects.create(
            insumo=insumo,
      
            total=stock_actual,
            cantidadTomada=cantidadTomada
        )
        return redirect('/')
    else: 
        raise ValueError("No hay suficiente stock disponible.")
    
        


