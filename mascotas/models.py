from django.db import models
import uuid

class Mascota(models.Model):
    codigo = models.CharField(max_length=10, unique=True, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    edad_anios = models.IntegerField()
    edad_meses = models.IntegerField()
    edad_dias = models.IntegerField()
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre