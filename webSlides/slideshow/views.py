from django.shortcuts import render, redirect
from .models import Slides
from .forms import New_Slide_Form
from datetime import datetime
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')


def ShowSlides(request):
    slides = Slides.objects.all()
    is_admin = request.user.is_staff
    if request.method == 'GET':
        return render(request, 'home.html', {
            'slides': slides,
            'admin': is_admin,
            'newSlide': New_Slide_Form()
        })
    else:
        CreateSlide(request)
        return redirect('slides:home')


def CreateSlide(request):
    slide = Slides.objects.create(
        title=request.POST['title'],
        details=request.POST['details'],
        content=request.POST['content'],
        date=datetime.now(),
        author=request.user
    )
    slide.save()


def Temporal(request):
    slide = Slides.objects.get(pk=6)
    return render(request, 'temporal.html', {
        'slides': ConvertToMD(slide.content),
    })


def ConvertToMD(content):
    lineas = content.strip().split('\n')
    resultado = []

    for linea in lineas:
        if linea.startswith('#'):  # Titulos
            level = linea.count('#')
            resultado.append(f"<h{level}>{linea[level:].strip()}</h{level}>")
        elif "**" in linea:  # Negritas
            while "**" in linea:
                inicio = linea.find("**")
                fin = linea.find("**", inicio+2)
                linea = linea[:inicio] + "<strong>" + \
                    linea[inicio+2:fin] + "</strong>" + linea[fin+2:]
            resultado.append(linea)
        elif "*" in linea:  # Negritas
            while "*" in linea:
                inicio = linea.find("*")
                fin = linea.find("*", inicio+1)
                linea = linea[:inicio] + "<em>" + \
                    linea[inicio+1:fin] + "</em>" + linea[fin+1:]
            resultado.append(linea)
        elif linea.startswith("- "):
            resultado.append(f"<li>{linea[2:].strip()}</li>")
        elif linea.startswith("http") or linea.startswith("https"):
            resultado.append(f"<img src='{linea}'>")
        else:
            resultado.append(linea)
    return resultado
