from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('update_info/<int:id>', views.update_info, name="update_info"),
    path('about', views.about, name="about"),
    path('upload_funtionary', views.upload_funtionary, name="upload_funtionary"),
    path('deleteData/<int:id>', views.deleteData, name="deleteData"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)