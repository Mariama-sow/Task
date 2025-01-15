from django import forms
from .models import Taches , Categorie


class TacheForm(forms.ModelForm) :

    class Meta :
        model = Taches
        fields = ('titre','description','date_echeance','priorite','categorie','status')
        widgets = {
            'titre' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Titre'}),
            'description' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'resume'}),
            'date_echeance' : forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder':'Date de publication','type': 'datetime-local'}),
            'priorite' : forms.Select(attrs={'class' : 'form-control', 'placeholder':'priorite'}),
            'categorie': forms.Select(attrs={'class' : 'form-control', 'placeholder':'categorie de la tache'}),
        }

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ('type',)

