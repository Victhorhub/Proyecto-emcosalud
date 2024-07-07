from django.urls import path
from . import views
#from core.views import RegisterData_View

urlpatterns = [
    path('', views.home, name="home"),
    path('update_info', views.update_info, name="update_info"),
    path('about', views.about, name="about"),
    #path('register_data', RegisterData_View.as_view(), name="add_data"),
    path('upload_funtionary', views.upload_funtionary, name="upload_funtionary"),
]
