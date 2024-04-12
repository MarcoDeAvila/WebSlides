from django.urls import path
from . import views

app_name = 'slides'

urlpatterns = [
    path('', views.ShowSlides, name='home'),
    path('<str:filename>/', views.Temporal, name='temporal'),
]