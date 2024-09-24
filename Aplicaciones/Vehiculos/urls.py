from django.urls import path
from . import views


urlpatterns = [
# rutas de modulos para navegacion
path('vehiculos/', views.vehiculos, name='vehiculos'),
path('mantenimientoVehiculos/<int:vehiculo_id>/', views.mantenimientoVehiculos, name='mantenimientoVehiculos'),

]

