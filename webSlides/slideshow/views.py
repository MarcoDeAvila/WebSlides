from django.shortcuts import render, redirect
from .forms import New_Slide_Form, Edit_Slide_Form
from django.contrib.auth.models import User
import os
import markdown
from django.http import JsonResponse
from django.utils.text import slugify

# Create your views here.

def home(request):
    return render(request, 'home.html')

def ShowSlides(request):
    directorio = 'SlideFiles'
    if not os.path.exists(directorio):
        os.makedirs(directorio)
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
        title = request.POST.get('title', 'Untitled')
        content = request.POST.get('content', '')
        author = request.user.username if request.user.is_authenticated else 'Anonymous'

        # Asegurarse de que el directorio existe
        directory = 'SlideFiles'
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Nombre del archivo
        filename = f"{title}.txt"
        path = os.path.join(directory, filename)

        # Guardar el contenido como archivo de texto
        with open(path, 'w') as SlideFile:
            SlideFile.write(author + '\n')
            SlideFile.write(content)

        return redirect('slides:home')
    else:
        return render(request, 'nueva.html')

def UploadSlide(request):
    if request.method == 'POST':
        author = request.user.username if request.user.is_authenticated else 'Anonymous'

        # Asegurarse de que el directorio existe
        directory = 'SlideFiles'
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Guardar el archivo subido
        if 'file' in request.FILES and request.FILES['file']:
            uploaded_file = request.FILES['file']
            title = request.POST.get('title', os.path.splitext(uploaded_file.name)[0])
            filename = f"{slugify(title)}.txt"
            path = os.path.join(directory, filename)

            # Leer el contenido del archivo subido
            file_content = uploaded_file.read().decode('utf-8')

            # Procesar el contenido para eliminar saltos de línea adicionales
            cleaned_content = "\n".join([line for line in file_content.splitlines() if line.strip() != ""])

            # Escribir el contenido con el autor al principio
            with open(path, 'w') as destination:
                destination.write(author + '\n')
                destination.write(file_content)

        return redirect('slides:home')
    else:
        return redirect('slides:home')

def Presentacion(request, filename):
    path = f'SlideFiles/{filename}.txt'
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
    
def Eliminar(request, filename):
    try:
        path = f'Slidefiles/{filename}.txt'
        os.remove(path)
        return redirect('slides:home')
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
