from .models import Rezervare
from rest_framework import serializers

class RezervareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rezervare
        fields = ['nume', 'prenume', 'email_sau_telefon', 'data', 'ora']