from django.urls import path
from task.views import home, about, contact, upload_photo, gallery

urlpatterns = [
    path("", home, name="homew"),
    path("about/", about, name="aboutw"),
    path("contact/", contact, name="contacty"),
    path("upload_photo/", upload_photo, name="upload_photo"),  # Ruta para subir fotos
    path("gallery/", gallery, name="gallery"),
]
