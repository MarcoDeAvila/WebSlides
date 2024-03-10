from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
# Create your views here.

def home(request):
    return HttpResponse("<h1>Pagina de bienvenida</h1>")

def login(request):
    return render(request, 'users/login.html')
