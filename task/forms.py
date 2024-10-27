# task/forms.py
from django import forms
from .models import Photo, Photo2

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo # Modelo al que pertenece el formulario
        fields = ['title', 'image']
        
class PhotoForm2(forms.ModelForm):
    class Meta:
        model = Photo2 # Modelo al que pertenece el formulario
        fields = ['title', 'image']