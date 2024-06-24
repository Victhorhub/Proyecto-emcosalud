from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('update_info', views.update_info, name="update_info"),
    path('about', views.about, name="about"),
    path('add_data', views.add_data, name="add_data"),
]
