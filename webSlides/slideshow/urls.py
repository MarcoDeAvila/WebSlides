from django.urls import path
from . import views

app_name = 'slides'

urlpatterns = [
    path('', views.ShowSlides, name='home'),
    path('/<str:filename>/', views.Presentacion, name='temporal'),
    path('nueva/', views.CreateSlide, name='nueva'),
    path('editar/', views.Editar, name='editar'),
    path('editar/eliminar/', views.Eliminar, name='editar'),
]