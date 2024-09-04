from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('registrarInsumo/', views.registrarInsumo),
    path('edicionInsumo/<codigo>', views.edicionInsumo),
    path('editarInsumo/', views.editarInsumo),
    path('eliminacionInsumo/<codigo>', views.eliminacionInsumo),
    
]