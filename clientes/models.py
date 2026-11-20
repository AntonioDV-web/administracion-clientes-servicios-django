from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    fotografia = models.ImageField(upload_to="clientes/", blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
