from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.signIn, name='signin'),  # Inicio sesion
    path('signup/', views.signUp, name='signup'),  # Registrarse
    path('logout/', views.singOut, name='logout'),  # Home
]