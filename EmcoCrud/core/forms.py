from django import forms
from core.models import Funtionary, Headquarters
from django.contrib.auth.forms import  UserCreationForm


class FuntionaryForm(forms.ModelForm):
    class Meta:
        model = Funtionary
        fields = ("identification", "name", "lastname", "birthday", "telephone", "email", "active"
        , "speciality", "curriculum", "diploma", "Retus", "courses", "degree_certificate", "title", "contract"
        , "type_vinculation", "policy", "tariff", "Headquarters")


# class FuntionaryForm(forms.ModelForm):
#     funtionary_headquarters = forms.ModelMultipleChoiceField(
#         queryset=Headquarters.objects.all(),
#         widget=forms.SelectMultiple,
#     )
