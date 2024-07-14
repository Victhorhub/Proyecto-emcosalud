from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Funtionary
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from openpyxl import Workbook
from openpyxl.styles import *
import decimal
from  django import forms
from .forms import FuntionaryForm
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.utils.timezone import localtime
import pandas as pd
from django.db.models import F
# Create your views here.


def home(request):
    funtionary_ = Funtionary.objects.all()
    return render(request, "core/home.html", {"funtionary_" : funtionary_})

def update_info(request):
    return render(request, "core/update_info.html")

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