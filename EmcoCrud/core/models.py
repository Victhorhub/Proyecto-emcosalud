from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

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

class Headquarters(models.Model):
    nameHeadquarter = models.CharField(max_length=200, verbose_name="Nombre de la sede")
    Direction = models.CharField(max_length=200, verbose_name="Direccion de la sede")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sede"
        verbose_name_plural = "Sedes"
        ordering = ["-created"]

    def __str__(self):
        return self.nameHeadquarter


class Speciality(models.Model):
    title = models.CharField(max_length=200, verbose_name="Especialidad")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"
        ordering = ["-created"]

    def __str__(self):
        return self.title


# Funtionary model
class Funtionary(models.Model):
    identification = models.IntegerField()
    name = models.CharField(max_length=200, verbose_name="Nombre del funcionario")
    lastname = models.CharField(max_length=200, verbose_name="Apellido del funcionario")
    birthday=models.DateField(verbose_name='Fecha de nacimiento')
    telephone = models.CharField(max_length=10, verbose_name="Numero de celular")
    email = models.EmailField(max_length=200, verbose_name="Correo electronico")
    active = models.BooleanField(default=True, verbose_name="Activo")
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE , max_length=200, verbose_name="Especialidad")
    #Curriculum docs
    curriculum = models.FileField(upload_to= 'curriculum/',verbose_name="Hoja de vida", default="upload your cirriculum")
    diploma = models.FileField(upload_to= 'diploma/',verbose_name="Diploma", default="upload your diploma")
    Retus = models.FileField(upload_to= 'Retus/',verbose_name="Retus", default = "upload your retus")
    courses = models.FileField(upload_to= 'courses/',verbose_name="Cursos", default="upload your courses")
    degree_certificate = models.FileField(upload_to= 'degree_certificate/',verbose_name="Acta de grado", default="upload your degree certificate")
    title = models.FileField(upload_to= 'title/',verbose_name="Convalidacion titulo icfes", default="upload your title")
    #Contract
    contract = models.FileField(upload_to= 'contract/',verbose_name="Contrato", default="upload your contract")
    type_vinculation = models.CharField(max_length=100, verbose_name="Tipo de vinculacion", null=True)
    policy = models.FileField(upload_to= 'policy/',verbose_name="Poliza", default="upload your poliza")
    tariff = models.IntegerField(null=True, verbose_name="Tarifa")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    Headquarters = models.ManyToManyField(Headquarters, verbose_name="Sede")

    @property
    def age(self):
        today = date.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

    # @property
    # def state(self):
    #     state = null
    #     if (active == True):
    #         state = "Activo"
    #     else:
    #         state = "Inactivo"
    #     return state

    class Meta:
        verbose_name = "Funcionario"
        verbose_name_plural = "Funcionarios"
        ordering = ["-created"]

    def __str__(self):
        return self.name