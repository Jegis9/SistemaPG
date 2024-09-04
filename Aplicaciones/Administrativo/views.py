from django.shortcuts import render, redirect
from .models import Insumos, InsumoLog
from django.contrib.auth.decorators import login_required #importa libreria para hacer de la pagina requerido el login para poder verla
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    insumosList = Insumos.objects.all()
    return render(request, "insumos.html", {"insumos": insumosList})

def usuarios(request):
    # Obtenemos la lista de todos los usuarios registrados
    users = User.objects.all()
    return render(request, 'usuarios.html', {"object_list": users})

# def insumos(request):
#     return render(request, 'insumos.html')

@login_required
def registrarInsumo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        stock_inicial = request.POST.get('cantidadInicial')
     

        Insumos.objects.create(nombre=nombre, stock_inicial=stock_inicial, stock_actual=stock_inicial)

        return redirect('/')
    else:
        return redirect('/')
    

@login_required
def eliminacionInsumo(request, codigo):
    insumo = Insumos.objects.get(codigo=codigo)
    insumo.delete()
    
    return redirect('/')







@login_required
def edicionInsumo(request, codigo):
    insumo = Insumos.objects.get(codigo=codigo)
    return render(request, "insumosEditar.html", {"insumo": insumo})


@login_required
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
    
        


