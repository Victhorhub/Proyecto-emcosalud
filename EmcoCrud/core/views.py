from django.shortcuts import render, redirect, get_object_or_404
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