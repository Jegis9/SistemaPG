from django.shortcuts import render, redirect
from .models import Insumos, InsumoLog
from django.contrib.auth.decorators import login_required #importa libreria para hacer de la pagina requerido el login para poder verla
from django.contrib.auth.models import User
# importar libreria para el registro de usuarios
from django.contrib.auth.forms import UserCreationForm
from Aplicaciones.user.forms import CreateUserForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views import View


# Create your views here.

def home(request):
    insumosList = Insumos.objects.all()
    return render(request, "insumos.html", {"insumos": insumosList})

def usuarios(request):
    # Obtenemos la lista de todos los usuarios registrados
    users = User.objects.all()
    return render(request, 'usuarios.html', {"object_list": users})


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
    
        




def nuevo_registro(request):
    if request.method == 'POST':# si el metodo es POST (recibe datos)
        form = CreateUserForm(request.POST)#entonces que cree o reciba los parametros de post
        if form.is_valid():# si estos son validos entonces
            user = form.save()# los guarda
            # aqui se manda a llamar al modelo de perfil con su campo relacionado de usuario que se creara
            profile = user.profile
            profile.is_internal = form.cleaned_data.get('is_internal', True) # aqui se define si el perfil del usuario es true o false, debido a que es un usuario externo se dejara en False
            profile.save() # aqui se guarda el perfil del usuario relacionado con el campo is_internal como False
            messages.success(request, 'Nuevo usuario agregado correctamente')
            
    else:
        form = CreateUserForm() # si el formulario no es POST (envio de datos) y es GET (carga la pagina)


    context = {'formulario': form}
    return render(request, 'nuevo_registro.html', context)

