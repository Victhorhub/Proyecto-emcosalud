from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Funtionary
from  django import forms
from .forms import FuntionaryForm
from django.views.generic import CreateView
from django.views.generic import TemplateView

# Create your views here.


def home(request):
    funtionary_ = Funtionary.objects.all()
    #age = funtionary_.age()
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


def deleteData(request,id):
    funtionary_ = Funtionary.objects.get(id=id)
    funtionary_.delete()
    return redirect('home')