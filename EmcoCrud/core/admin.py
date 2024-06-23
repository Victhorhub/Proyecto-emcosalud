from django.contrib import admin
from .models import Country, State, City, Headquarters, Speciality, Funtionary

# Register your models here.
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Headquarters)
admin.site.register(Speciality)
admin.site.register(Funtionary)