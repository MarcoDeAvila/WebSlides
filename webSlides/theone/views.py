from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import SignIn_User, SignUp_User
from slideshow.views import home

# Create your views here.


def signUp(request):
    if request.method == 'GET':
        return render(request, 'signUp.html', {
            'form': SignUp_User()
        })
    else:
        if request.POST['password'] == request.POST['confirmPassword']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    email=request.POST['email'],
                    password=request.POST['password']
                )
                user.save()
                login(request, user)
                return redirect('slides:home')
            except:
                return render(request, 'signUp.html', {
                    'form': SignUp_User(),
                    'error': 'Username already exists.'
                })
        else:
            return render(request, 'signUp.html', {
                'form': SignUp_User(),
                'error': 'Password do not match.'
            })


def signIn(request):
    if request.method == "GET":
        return render(request, 'signin.html', {
            'form': SignIn_User()
        })
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password']
                            )
        if user is None:
            return render(request, 'signin.html', {
                'form': SignIn_User(),
                'error': 'Username or password is incorrect.'
            })
        else:
            login(request, user)
            return redirect('slides:home')


def singOut(request):
    logout(request)
    return redirect('usuarios:signin')
