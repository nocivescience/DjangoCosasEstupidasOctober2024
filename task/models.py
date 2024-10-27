# task/models.py
from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=100)  # Un título opcional para la imagen
    image = models.ImageField(upload_to='photos/')  # Campo para la imagen
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Fecha de subida

    def __str__(self):
        return self.title
