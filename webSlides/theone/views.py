from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.template import Template, Context
# Create your views here.

def home(request):
    return HttpResponse("<h1>Pagina de bienvenida</h1>")

def signin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('user')
            messages.success(request, 'Hola ' + username + ' tu cuenta ha sido creada exitosamente')
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request,'users/signin.html')

def login(request):
    return render(request, 'users/login.html')
