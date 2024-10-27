from django.urls import path
from task.views import home, about, contact, upload_photo, gallery, gallery_2, upload_photo_2
urlpatterns = [
    path("", home, name="homew"),
    path("about/", about, name="aboutw"),
    path("contact/", contact, name="contacty"),
    path("upload_photo/", upload_photo, name="upload_photo"),  # Ruta para subir fotos
    path("gallery/", gallery, name="gallery"),
    path("upload_photo_2/", upload_photo_2, name="upload_photo_2"),  # Ruta para subir fotos
    path("gallery_2/", gallery_2, name="gallery_2"),
]
