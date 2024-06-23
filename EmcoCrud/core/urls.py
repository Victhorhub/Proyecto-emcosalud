from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloworld, name="home"),
    path('update_info', views.update_info, name="update_info"),
    path('about', views.about, name="about"),
]
