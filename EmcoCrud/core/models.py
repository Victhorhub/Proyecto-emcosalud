from django.db import models

# Create your models here.
from django.db import models

class Country(models.Model):
    nameCountry = models.CharField(max_length=200, verbose_name="Nombre del pais")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"
        ordering = ["-created"]

    def __str__(self):
        return self.nameCountry