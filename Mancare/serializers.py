from .models import Reteta
from rest_framework import serializers

class RetetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reteta
        fields = ['name', 'description',  'created', 'slug', 'price', 'category']