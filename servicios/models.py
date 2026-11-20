from django.db import models


class Servicio(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    fotografia = models.ImageField(upload_to="servicios/", blank=True, null=True)

    def __str__(self):
        return self.nombre
