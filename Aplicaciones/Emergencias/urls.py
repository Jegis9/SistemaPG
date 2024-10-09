from django.urls import path
from . import views
from .views import ServicioCreateView, ServicioListView, VariosListView,AmbulanciaListView,IncendiosListView

urlpatterns = [
    path('add/',ServicioCreateView.as_view(), name='add'),
    path('lista_servicios/', ServicioListView.as_view(), name='lista_servicios'),
    path('varios/', VariosListView.as_view(), name='varios'),
    path('ambulancia/', AmbulanciaListView.as_view(), name='ambulancia'),
    path('incendios/', IncendiosListView.as_view(), name='incendios'),
    # path('servicios/', views.lista_servicios, name='lista_servicios'),  # Nueva URL
    # path('servicios/varios/', views.lista_varios, name='lista_varios'),
    # path('servicios/ambulancia/', views.lista_ambulancia, name='lista_ambulancia'),
    # path('servicios/incendios/', views.lista_incendios, name='lista_incendios'),
]
