from django.urls import path
from . import views


urlpatterns = [
# rutas de modulos para navegacion
    
    path('epp/', views.epp, name='epp'),
path('estadoEPP/<int:asignado_id>/', views.estadoEPP, name='estadoEPP'),
path('lEpp/', views.lEpp, name='lEpp')
  
]