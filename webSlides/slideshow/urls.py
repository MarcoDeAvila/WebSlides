from django.urls import path
from . import views

urlpatterns = [
    path('slideshow/', views.slideShow, name='slideshow'),
    path('createslide/', views.createSlide, name='createslide'),
]

