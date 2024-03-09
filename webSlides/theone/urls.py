from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', views.plantilla),
    path('1/', views.plantilla),
]