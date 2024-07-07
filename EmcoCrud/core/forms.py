from django import forms
from core.models import Funtionary, Headquarters


class FuntionaryForm(forms.ModelForm):
    funtionary_headquarters = forms.ModelMultipleChoiceField(
        queryset=Headquarters.objects.all(),
        widget=forms.SelectMultiple,
    )
    
    class Meta:
        model = Funtionary
        fields = ("identification", "name", "lastname", "birthday", "telephone", "email", "active"
        , "speciality", "curriculum", "diploma", "Retus", "courses", "degree_certificate", "title", "contract"
        , "type_vinculation", "policy", "tariff", "funtionary_headquarters")