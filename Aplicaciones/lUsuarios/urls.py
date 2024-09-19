from django.urls import path
from . import views


urlpatterns = [
# rutas de modulos para navegacion
    
    path('lUsuarios/', views.lUsuarios, name='lUsuarios'),
    path('lInternos', views.lInternos, name='lInternos'),
    
  
]

