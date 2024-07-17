from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Funtionary, Speciality, Headquarters
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from openpyxl import Workbook
from openpyxl.styles import *
import decimal
from  django import forms
from .forms import FuntionaryForm
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.db.models import Q
from django.utils.timezone import localtime
import pandas as pd
from django.db.models import F
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')

# # Create your views here.
# def home(request):
#     return render(request, 'core/home.html')

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_query =  Q(Q(name__icontains=q) | Q(lastname__icontains=q))
        funtionary_query = Funtionary.objects.filter(multiple_query)
    else:
        funtionary_query = Funtionary.objects.all()
    context = {
        'funtionary_query' : funtionary_query
    }
    return render(request, "core/search.html", context)

# def filter_query(request):
#     funtionary_ = Funtionary.objects.all()
#     speciality_filter = Speciality.objects.all()
#     headquarters_filter = Headquarters.objects.all()
#     filter_speciality = request.GET.get('filter-speciality')
#     filter_headquarter = request.GET.get('filter-headquarter')

#     if is_valid_queryparam(filter_headquarter) and filter_headquarter != 'Choose...':
#         funtionary_ = funtionary_.filter(headquarters_filter__nameHeadquarter=filter_headquarter)

#     if is_valid_queryparam(filter_speciality) and filter_speciality != 'Choose...':
#         funtionary_ = funtionary_.filter(speciality_filter__title=filter_speciality)

#     context = {
#         'funtionary_query' : funtionary_query,
#         'speciality_filter' : speciality_filter,
#         'headquarters_filter' : headquarters_filter,
#     }
#     return render(request, "core/search.html", context)

def home(request):
    funtionary_ = Funtionary.objects.all()
    return render(request, "core/home.html", {"funtionary_" : funtionary_})

def about(request):
    return render(request, "core/about.html")

def upload_funtionary(request):
    if request.method == 'POST':
        form = FuntionaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FuntionaryForm()
    context = {
        'form': form,
    }
    return render(request, 'core/add_data.html', context)


def deleteData(request,id):
    funtionary_ = Funtionary.objects.get(id=id)
    funtionary_.delete()
    return redirect('home')


def update_info(request, id):
    funtionary_ = get_object_or_404(Funtionary, id=id)
    if request.method == 'POST':
        form = FuntionaryForm(request.POST, request.FILES, instance=funtionary_)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FuntionaryForm(instance=funtionary_)
    return render(request, 'core/update_info.html', {'form': form})

def export_to_excel(request):
    # Obtener los datos de los funcionarios con los campos necesarios
    funcionarios = Funtionary.objects.all()

    # Lista de campos que deseas exportar
    campos_exportar = [
        'identification', 'name', 'lastname', 'birthday', 'telephone', 'email', 'active',
        'speciality__title'
    ]

    # Obtener los datos y renombrar el campo especialidad
    datos = funcionarios.values(
        *campos_exportar
    ).annotate(
        headquarters_list=F('Headquarters__nameHeadquarter')
    )

    # Crear el DataFrame de pandas
    df = pd.DataFrame(datos)

    # Renombrar la columna 'speciality__title' a 'speciality' si es necesario
    df.rename(columns={'speciality__title': 'speciality__title'}, inplace=True)

    # Asegurarse de que las fechas estén en el formato correcto sin zona horaria
    df['birthday'] = pd.to_datetime(df['birthday']).dt.tz_localize(None)

    # Agrupar todas las filas por los campos especificados en campos_exportar
    df_final = df.groupby(campos_exportar).agg({
        'headquarters_list': ', '.join
    }).reset_index()

    # Diccionario para renombrar las columnas al español
    columnas_esp = {
        'identification': 'Identificación',
        'name': 'Nombre',
        'lastname': 'Apellido',
        'birthday': 'Fecha de Nacimiento',
        'telephone': 'Teléfono',
        'email': 'Correo Electrónico',
        'active': 'Activo',
        'speciality': 'Especialidad',
        'headquarters_list': 'Lista de Sedes'
    }

    # Renombrar las columnas en el DataFrame
    df_final.rename(columns=columnas_esp, inplace=True)

    # Crear un objeto HttpResponse con el tipo de contenido adecuado
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=funcionarios.xlsx'

    # Utilizar pandas para escribir los datos a un archivo de Excel en el response
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df_final.to_excel(writer, index=False, sheet_name='Funcionarios')

    return response

@login_required
def products(request):
    return render(request, 'core/products.html')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('login')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)

