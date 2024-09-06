from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('reportEmergency/', views.reportEmergency, name='reportEmergency'),

    path('profile/', views.profile, name='profile' )
]+ static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #url para aceptar imagenes 



