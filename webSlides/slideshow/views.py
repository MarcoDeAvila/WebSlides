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
    presentaciones = []
    autores = []

    for filename in os.listdir(directorio):
        if filename.endswith('.txt'):
            path = os.path.join(directorio, filename)
            presentacion_nombre = filename.replace('.txt', '')
            with open(path, 'r') as file:
                primer_linea = file.readline().strip()
                autores.append(primer_linea)
            presentaciones.append(presentacion_nombre)

    is_admin = request.user.is_superuser
    author = request.user.username

    if request.method == 'GET':
        presentaciones_con_autores = zip(presentaciones, autores)
        return render(request, 'home.html', {
            'presentaciones_con_autores': presentaciones_con_autores,
            'newSlide': New_Slide_Form(),
            'edit': Edit_Slide_Form()
        })


def CreateSlide(request):
    if request.method == 'POST':
        title = request.POST['title']
        path = 'SlideFiles/'+title+'.txt'
        content = request.POST['content']
        author = request.user.username

        with open(path, 'w') as SlideFile:
            SlideFile.write(author + '\n')
            SlideFile.write(content)

        return redirect('slides:home')
    else:
        return render(request, 'nueva.html', {
            'newSlide': New_Slide_Form(),
        })
        

def Presentacion(request, filename):
    path = f'Slidefiles/{filename}.txt'
    with open(path, 'r') as file:
        lines = file.readlines()

    # Excluir la primera línea que contiene el nombre de usuario
    content = ''.join(lines[1:])

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
        newTitle = request.POST['title']
        if newTitle != filename:
            new_path = f'Slidefiles/{newTitle}.txt'
            os.rename(path, new_path)
        else:
            new_path = path

        content = request.POST['content']
        author = request.user.username

        new_content = f"{author}\n{content}"

        with open(new_path, 'w') as file:
            file.write(new_content)
        return redirect('slides:home')
    else:
        with open(path, 'r') as file:
            lines = file.readlines()[1:]
            content = ''.join(lines)

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
