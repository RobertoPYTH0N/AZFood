from django import forms
from .models import Rezervare

class FormularRezervare(forms.ModelForm):
    class Meta:
        model = Rezervare
        fields = ['nume', 'prenume', 'email_sau_telefon', 'data', 'ora']
        widgets = {
            'nume': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nume'}),
            'prenume': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prenume'}),
            'email_sau_telefon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email sau Telefon'}),
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'ora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }