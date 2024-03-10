from django.urls import path
from . import views

urlpatterns = [
    path('', views.signIn, name='signin'), # Inicio sesion
    path('signup/',views.signUp, name='signup'), # Registrarse
    path('home/',views.home, name='home'), # Home
    path('logout/',views.singOut, name='logout'), # Home
]

