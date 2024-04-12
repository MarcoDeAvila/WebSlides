from django.shortcuts import render, redirect
from .forms import New_Slide_Form
import os
# Create your views here.


def home(request):
    return render(request, 'home.html')


def ShowSlides(request):

    directorio = 'SlideFiles'
    lista_presentaciones = []

    for filename in os.listdir(directorio):
        if filename.endswith('.txt'):
            lista_presentaciones.append(filename.replace('.txt', ''))

    is_admin = request.user.is_staff
    if request.method == 'GET':
        return render(request, 'home.html', {
            'presentaciones': lista_presentaciones,
            'admin': is_admin,
            'newSlide': New_Slide_Form()
        })
    else:
        CreateSlide(request)
        return redirect('slides:home')


def CreateSlide(request):
    title = request.POST['title']
    path = 'SlideFiles/'+title+'.txt'
    SlideFile = open(path, 'x')
    SlideFile =  open(path, 'w')
    SlideFile.writelines(request.POST['content'])
    SlideFile.close()



def Temporal(request, filename):
    path = f'Slidefiles/{filename}.txt'
    with open(path, 'r') as file:
        content = file.read()

    slides = content.split("/Fin")

    slidesMD = []
    for slide in slides:
        slidesMD.append(ConvertToMD(slide))

    return render(request, 'temporal.html', {'slides': slidesMD})


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
