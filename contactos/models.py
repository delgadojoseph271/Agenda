from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from django.conf import settings

class Contacto(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='contactos')
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    numero_telefono = models.CharField(max_length=15)
    notas = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre
