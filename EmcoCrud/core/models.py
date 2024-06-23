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

class State(models.Model):
    nameState = models.CharField(max_length=200, verbose_name="Nombre del estado")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Estados/Departamentos"
        verbose_name_plural = "Estado/Departamentos"
        ordering = ["-created"]

    def __str__(self):
        return self.nameState

class City(models.Model):
    nameCity = models.CharField(max_length=200, verbose_name="Nombre de la ciudad")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        ordering = ["-created"]

    def __str__(self):
        return self.nameCity