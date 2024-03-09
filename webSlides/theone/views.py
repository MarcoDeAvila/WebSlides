from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
# Create your views here.
def bienvenida(request):
    return HttpResponse("Prueba 1")
def plantilla(request):
    #FIXME
    plantilaExt = open('C:/Users/fede1/Documents/Repositorios/WebSlides/webSlides/plantilla/login.html')
    #plantilaExt = open('/webSlides/plantilla/login.html')
    # No se por que no jala con la ruta relativa

    template = Template(plantilaExt.read())
    plantilaExt.close()
    contexo = Context()
    documento = template.render(contexo)
    return HttpResponse(documento)
