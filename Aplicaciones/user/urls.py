from django.urls import path
from . import views
from .views import CustomLoginView

# rutas que serviran para poder manejar las rutas de esta aplicacion


urlpatterns = [
    path('landingPage/', views.landingPage, name='landingPage'),
    path('register/', views.register, name='register' ),
    path('logout/', views.logout, name='logout' ),
    path('login/', CustomLoginView.as_view(), name='login'),

]


