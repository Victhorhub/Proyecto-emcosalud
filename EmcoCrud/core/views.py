from django.shortcuts import render
from django.http import HttpResponse
from .models import Funtionary
from  django import forms
from .forms import FuntionaryForm
from django.views.generic import CreateView
from django.views.generic import TemplateView

# Create your views here.


def home(request):
    funtionary_ = Funtionary.objects.all()
    return render(request, "core/home.html", {"funtionary_" : funtionary_})

def update_info(request):
    return render(request, "core/update_info.html")

def about(request):
    return render(request, "core/about.html")


class RegisterData_View(CreateView):
    form_class = FuntionaryForm
    template_name = "core/add_data.html"

    def get_form(self, form_class=None):
        form = super (RegisterData_View, self).get_form()
        form.fields['identification'].widget = forms.NumberInput( attrs = {'class': 'form-control mb-2', "placeholder": 'Identificacion'})
        form.fields['name'].widget = forms.TextInput( attrs = {'class': 'form-control mb-2', "placeholder": 'Nombre'})
        form.fields['lastname'].widget = forms.TextInput( attrs = {'class': 'form-control mb-2', "placeholder": 'Apellido'})
        form.fields['birthday'].widget = forms.DateInput( attrs = {'class': 'form-control mb-2', "placeholder": 'Fecha de Nacimiento'})
        form.fields['telephone'].widget = forms.TextInput( attrs = {'class': 'form-control mb-2', "placeholder": 'Telefono'})
        form.fields['email'].widget = forms.EmailInput( attrs = {'class': 'form-control mb-2', "placeholder": 'Email'})
        form.fields['active'].widget = forms.CheckboxInput( attrs = {'class': 'form-control mb-2'})
        form.fields['speciality'].widget = forms.Select( attrs = {'class':'form-select'})
        form.fields['curriculum'].widget = forms.FileInput( attrs = {'class': 'form-control mb-2', "type": 'file', 'id': 'formFile'})
        form.fields['diploma'].widget = forms.FileInput( attrs = {'class': 'form-control mb-2', "type": 'file', 'id': 'formFile'})
        form.fields['Retus'].widget = forms.FileInput( attrs = {'class': 'form-control mb-2', "type": 'file', 'id': 'formFile'})
        form.fields['courses'].widget = forms.FileInput( attrs = {'class': 'form-control mb-2', "type": 'file', 'id': 'formFile'})
        form.fields['degree_certificate'].widget = forms.FileInput( attrs = {'class': 'form-control mb-2', "type": 'file', 'id': 'formFile'})
        form.fields['title'].widget = forms.FileInput( attrs = {'class': 'form-control mb-2', "type": 'file', 'id': 'formFile'})
        form.fields['contract'].widget = forms.FileInput( attrs = {'class': 'form-control mb-2', "type": 'file', 'id': 'formFile'})
        form.fields['policy'].widget = forms.FileInput( attrs = {'class': 'form-control mb-2', "type": 'file', 'id': 'formFile'})
        form.fields['tariff'].widget = forms.NumberInput( attrs = {'class': 'form-control mb-2', "placeholder": 'Tarifa'})
        form.fields['Headquarters'].widget = forms.SelectMultiple( attrs = {'class': 'form-select' , 'multiple aria-label': 'Multiple select example'})
        #Labels
        form.fields['identification'].label = 'Identificacion'
        form.fields['name'].label = 'Nombre'
        form.fields['lastname'].label = 'Apellido'
        form.fields['birthday'].label = 'Fecha de nacimiento'
        form.fields['telephone'].label = 'telefono'
        form.fields['email'].label = 'Correo electronico'
        form.fields['active'].label = 'Estado'
        form.fields['speciality'].label = 'Especialidad'
        form.fields['curriculum'].label = 'Hoja de Vida'
        form.fields['diploma'].label = 'Diploma'
        form.fields['Retus'].label = 'Retus'
        form.fields['courses'].label = 'Cursos'
        form.fields['degree_certificate'].label = 'Certificado de grado'
        form.fields['title'].label = 'Titulo'
        form.fields['contract'].label = 'Contrato'
        form.fields['policy'].label = 'Poliza'
        form.fields['tariff'].label = 'Tarifa'
        form.fields['Headquarters'].label = 'Sede'
        return form