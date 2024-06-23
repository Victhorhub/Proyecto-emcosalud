from django.shortcuts import render
from django.http import HttpResponse
from .models import Funtionary

# Create your views here.


def home(request):
    funtionary_ = Funtionary.objects.all()
    return render(request, "core/home.html", {"funtionary_" : funtionary_})

def update_info(request):
    return render(request, "core/update_info.html")

def about(request):
    return render(request, "core/about.html")