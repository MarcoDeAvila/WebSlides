from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroFormulario
from django.contrib import messages
from django.template import Template, Context
# Create your views here.

def home(request):
    return HttpResponse("<h1>Pagina de bienvenida</h1>")

def signin(request):
    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroFormulario()
    return render(request,'users/signin.html', {'form': form})

def login(request):
    return render(request, 'users/login.html')
