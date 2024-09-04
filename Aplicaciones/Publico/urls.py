from django.urls import path
from . import views


urlpatterns = [
    path('reportEmergency/', views.reportEmergency, name='reportEmergency'),


]



