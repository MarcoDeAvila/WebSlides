from django.urls import path
from . import views

app_name = 'slides'

urlpatterns = [
    path('', views.ShowSlides, name='home'),
    path('temporal/', views.Temporal, name='temporal'),
]

