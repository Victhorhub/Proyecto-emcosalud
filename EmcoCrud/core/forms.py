from django import forms
from core.models import Funtionary, Headquarters
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User


class FuntionaryForm(forms.ModelForm):
    class Meta:
        model = Funtionary
        fields = ("identification", "name", "lastname", "birthday", "telephone", "email", "active"
        , "speciality", "curriculum", "diploma", "Retus", "courses", "degree_certificate", "title", "contract"
        , "type_vinculation", "policy", "tariff", "Headquarters")



class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
	def clean_email(self):
		email = self.cleaned_data['email']

		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Este correo electrónico ya está registrado')
		return email

