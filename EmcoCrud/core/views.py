from django.shortcuts import render
from django.http import HttpResponse
from .models import Funtionary
from core.forms import FuntionaryForm
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
        form.fields['identification'].widget = forms.IntegerField( attrs = {'class': 'form-control mb-2', "placeholder": 'Identificacion'})
        form.fields['name'].widget = forms.CharField( attrs = {'class': 'form-control mb-2', "placeholder": 'Nombre'})
        form.fields['lastname'].widget = forms.CharField( attrs = {'class': 'form-control mb-2', "placeholder": 'Apellido'})
        form.fields['birthday'].widget = forms.DateField( attrs = {'class': 'form-control mb-2', "placeholder": 'Fecha de Nacimiento'})
        form.fields['telephone'].widget = forms.CharField( attrs = {'class': 'form-control mb-2', "placeholder": 'Telefono'})
        form.fields['EmailField'].widget = forms.EmailField( attrs = {'class': 'form-control mb-2', "placeholder": 'Email'})
        form.fields['active'].widget = forms.IntegerField( attrs = {'class': 'form-control mb-2'})
        form.fields['BooleanField'].widget = forms.BooleanField( attrs = {'class': 'form-control mb-2'})
        form.fields['speciality'].widget = forms.ForeignKey( attrs = {'class="form-select"'})
        form.fields['curriculum'].widget = forms.FileField( attrs = {'class': 'form-control mb-2', "type": 'file', 'id': 'formFile'})
        form.fields['diploma'].widget = forms.FileField( attrs = {'class': 'form-control mb-2', "type": 'file', 'id': 'formFile'})
        form.fields['Retus'].widget = forms.FileField( attrs = {'class': 'form-control mb-2', "type": 'file', 'id': 'formFile'})
        form.fields['courses'].widget = forms.FileField( attrs = {'class': 'form-control mb-2', "type": 'file', 'id': 'formFile'})
        form.fields['degree_certificate'].widget = forms.FileField( attrs = {'class': 'form-control mb-2', "type": 'file', 'id': 'formFile'})
        form.fields['title'].widget = forms.FileField( attrs = {'class': 'form-control mb-2', "type": 'file', 'id': 'formFile'})
        form.fields['contract'].widget = forms.FileField( attrs = {'class': 'form-control mb-2', "type": 'file', 'id': 'formFile'})
        form.fields['policy'].widget = forms.FileField( attrs = {'class': 'form-control mb-2', "type": 'file', 'id': 'formFile'})
        form.fields['tariff'].widget = forms.IntegerField( attrs = {'class': 'form-control mb-2', "placeholder": 'Tarifa'})
        form.fields['Headquarters'].widget = forms.ForeignKey( attrs = {'class="form-select" multiple aria-label="Multiple select example"'})


"""

"", "", "", "", "", "", ""
        , "", "", "", "", "", "", "", ""
        , "", "", "", ""

"""

# def add_data(request):
#     context = {'form': FuntionaryForm()}
#     return render(request, "core/add_data.html", context)