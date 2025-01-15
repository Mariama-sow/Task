from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        widgets = {
                'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}),
                'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre prenom'}),
                'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom_utilisateur'}),
                'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre adresse email'}),
                'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'votre mot de passe'}),
            }


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom_utilisateur'}),)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder' : 'votre mot de passe',}), min_length=8 )