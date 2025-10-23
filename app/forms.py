from django.shortcuts import render, redirect 
# forms.py
from django import forms
from .models import Paciente
from .models import Entrevista


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['dni_paciente', 'nombre', 'apellido', 'fecha_nacimiento', 'sexo', 'telefono', 'email']

class EntrevistaForm(forms.ModelForm):
    class Meta:
        model = Entrevista
        fields = '__all__'
