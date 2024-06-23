from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, "core/base.html")

def update_info(request):
    return render(request, "core/update_info.html")

def about(request):
    return render(request, "core/about.html")