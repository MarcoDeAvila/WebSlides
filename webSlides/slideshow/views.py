from django.shortcuts import render, redirect
from .forms import New_Slide_Form, Edit_Slide_Form
from django.contrib.auth.models import User
import os
import markdown
from django.http import JsonResponse

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
            'edit': Edit_Slide_Form()
        })


def CreateSlide(request):
    if request.method == 'POST':
        title = request.POST['title']
        path = 'SlideFiles/'+title+'.txt'
        SlideFile = open(path, 'x')
        SlideFile =  open(path, 'w')
        SlideFile.writelines(request.POST['content'])
        SlideFile.close()
        return redirect('slides:home')
    else:
        return render(request, 'nueva.html', {
            'newSlide': New_Slide_Form(),
        })
        

def Presentacion(request, filename):
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

def Editar(request):
    filename = request.GET.get('filename', None)
    path = f'Slidefiles/{filename}.txt'
    
    if request.method == 'POST':
        os.rename(path, request.POST['title'])
        with open(path, 'w') as file:
            file.write(request.POST['content'])
        return redirect('slides:home')
    else:
        with open(path, 'r') as file:
            content = file.read()
        return render(request, 'editar.html', {
            'edit': Edit_Slide_Form(),
            'content': content, 
            'title': filename
        })
    
def Eliminar(request):
    try:
        filename = request.GET.get('filename', None)
        path = f'Slidefiles/{filename}.txt'
        os.remove(path)
        return JsonResponse({'message': 'Archivo eliminado correctamente'}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
