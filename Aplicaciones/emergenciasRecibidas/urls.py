from django.urls import path
from . import views


urlpatterns = [
# rutas de modulos para navegacion
    
    path('EmergenciasReportadas/', views.EmergenciasReportadas, name='EmergenciasReportadas'),


]