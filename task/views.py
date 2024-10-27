from django.shortcuts import render, redirect
from .forms import PhotoForm, PhotoForm2
from .models import Photo, Photo2

# Create your views here.
def home(request):
    return render(request, 'task/home.html')

def about(request):
    return render(request, 'task/about.html')

def contact(request):
    return render(request, 'task/contact.html')

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')  # Redirige a una página para ver la galería de imágenes
    else:
        form = PhotoForm()
    return render(request, 'task/upload_photo.html', {'form': form})

def gallery(request):
    photos = Photo.objects.all()  # Obtén todas las imágenes
    return render(request, 'task/gallery.html', {'photos': photos})

def upload_photo_2(request):
    if request.method == 'POST':
        form = PhotoForm2(request.POST, request.FILES) # Crea un formulario con los datos de la petición POST y los archivos subidos (si los hay)
        if form.is_valid(): # Si el formulario es válido
            form.save() # Guarda los datos del formulario
            return redirect('gallery') # Redirige a una página para ver la galería de imágenes
    else:
        form = PhotoForm2() # Crea un formulario vacío
    return render(request, 'task/upload_photo.html', {'form': form}) # Renderiza la plantilla con el formulario vacío como contexto de la petición HTTP GET y el formulario con los datos de la petición POST y los archivos subidos (si los hay) como contexto de la petición HTTP POST

def gallery_2(request):
    photos = Photo2.objects.all() # Obtén todas las imágenes
    return render(request, 'task/gallery.html', {'photos': photos}) # Renderiza la plantilla con las imágenes como contexto de la petición HTTP GET