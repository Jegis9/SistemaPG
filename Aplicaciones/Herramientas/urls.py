from django.urls import path
from . import views


urlpatterns = [
# rutas de modulos para navegacion
    
    path('herramientas/', views.herramienta, name='herramientas'),
    path('estadoHerramienta/<int:herramienta_id>/', views.estadoHerramienta, name='estadoHerramienta'),
    path('lEHerramientas/', views.lEHerramientas, name='lEHerramientas'),
    path('marcar_arreglado/<int:codigo>', views.marcar_arreglado, name='marcar_arreglado'),


  
]