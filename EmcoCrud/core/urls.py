from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloworld),
    path('update_info', views.update_info),
    path('about', views.about),
]
