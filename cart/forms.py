from django import forms
from .models import InformatiiClient



QUANTITY_COICES =  ((f"{i}", f"{i} buca{'ți' if i > 1 else 'tă'}") for i in range(1, 11))

class AddToCartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=QUANTITY_COICES)

class FormularCumparatura(forms.ModelForm):

    class Meta:
        model = InformatiiClient
        fields = '__all__'

    
