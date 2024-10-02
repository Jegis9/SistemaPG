from django.urls import path
from . import views

urlpatterns = [
    path('agregar-servicio/', views.agregar_servicio, name='agregar_servicio'),
    path('servicios/', views.lista_servicios, name='lista_servicios'),  # Nueva URL
    path('servicios/varios/', views.lista_varios, name='lista_varios'),
    path('servicios/ambulancia/', views.lista_ambulancia, name='lista_ambulancia'),
    path('servicios/incendios/', views.lista_incendios, name='lista_incendios'),
]
