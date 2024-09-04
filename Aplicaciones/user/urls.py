from django.urls import path
from . import views


urlpatterns = [
    path('landingPage/', views.landingPage, name='landingPage'),
    path('register/', views.register, name='register' ),
    path('logout/', views.logout, name='logout' ),

]


