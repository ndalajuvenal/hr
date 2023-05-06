from django import forms
from .models import *
from datetime import datetime


class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = '__all__'
        labels = {
            'nom': 'nom',
            'mission': 'mission',
            'manager': 'manager',
        }

    def __init__(self, *args, **kwargs):
        super(DepartementForm, self).__init__(*args, **kwargs)


class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'
        labels = {
            'nom': 'denommination',
            'base': 'salaire de base',
        }

    def __init__(self, *args, **kwargs):
        super(CategorieForm, self).__init__(*args, **kwargs)


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        labels = {
            'nom': 'denommination',
            'mission': 'mission',
            'chef': 'chef',
            'departement': 'departement',
        }

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)


class FonctionForm(forms.ModelForm):
    class Meta:
        model = Fonction
        fields = '__all__'
        labels = {
            'nom': 'nom',
            'service': 'service',
            'categorie': 'categorie',
        }

    def __init__(self, *args, **kwargs):
        super(FonctionForm, self).__init__(*args, **kwargs)


class AgentForm(forms.ModelForm):
    required_css_class = 'required-field'
    error_css_class = 'error-field'

    class Meta:
        model = Agent
        fields = "__all__"
        widgets = {
            'naissance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'max': datetime.now().date()}),
            'embauche': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'max': datetime.now().date()})
        }

    def __init__(self, *args, **kwargs):
        super(AgentForm, self).__init__(*args, **kwargs)
