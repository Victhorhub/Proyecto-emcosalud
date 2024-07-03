from django import forms
from core.models import Funtionary


class FuntionaryForm(forms.ModelForm):
    class Meta:
        model = Funtionary
        fields = ("identification", "name", "lastname", "birthday", "telephone", "email", "active"
        , "speciality", "curriculum", "diploma", "Retus", "courses", "degree_certificate", "title", "contract"
        , "type_vinculation", "policy", "tariff", "Headquarters")