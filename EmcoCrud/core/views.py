from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

html_base = """
    <h1>EmcoCrud</h1>
    <ul>
        <li><a href="/">Inicio</a></li>
        <li><a href="/update_info">Actualizacion de datos</a></li>
        <li><a href="/about">Acerca de</a></li>
    </ul>
"""


def helloworld(request):
    return HttpResponse(html_base + """
        <h2>Inicio</h2>
        <p>Bienvenido al inicio</p>
    """)


def update_info(request):
    return HttpResponse(html_base + """
        <h2>Actualizacion de datos</h2>
        <p>Bienvenido al apartado de actualizacion de datos</p>
    """)

def about(request):
    return HttpResponse(html_base + """
        <h2>Acerca de </h2>
        <p>Esta una plataforma realizada durante las practicas</p>
    """)