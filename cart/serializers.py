from .models import InformatiiClient, Order
from rest_framework import serializers

class InformatiiClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformatiiClient
        fields = ['nume', 'prenume', 'email', 'adresa', 'numar_telefon', 'payment_method']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['customer', 'product', 'price', 'quantity']