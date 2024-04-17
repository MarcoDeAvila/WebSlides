from django.shortcuts import render, redirect
from .forms import New_Slide_Form, Search_User_Form
from django.contrib.auth.models import User
import os
#import markdown
# Create your views here.


def home(request):
    return render(request, 'home.html')


def ShowSlides(request):

    directorio = 'SlideFiles'
    lista_presentaciones = []

    for filename in os.listdir(directorio):
        if filename.endswith('.txt'):
            lista_presentaciones.append(filename.replace('.txt', ''))

    lista_Usuarios = User.objects.filter(is_superuser=False)

    is_admin = request.user.is_superuser

    if request.method == 'GET':
        return render(request, 'home.html', {
            'presentaciones': lista_presentaciones,
            'usuarios': lista_Usuarios,
            'admin': is_admin,
            'newSlide': New_Slide_Form(),
            'searchUser': Search_User_Form()
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
    md = markdown.Markdown(extensions=['markdown.extensions.extra'])
    # Convierte el contenido Markdown a HTML
    html_content = md.convert(content)
    return html_content
