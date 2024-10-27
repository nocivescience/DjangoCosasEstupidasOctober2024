from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo

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
