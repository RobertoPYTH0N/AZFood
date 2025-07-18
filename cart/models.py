from django.db import models
from .processor import *
from cart import *
from Mancare.models import Reteta

# Create your models here.

PAYMENT_CHOICES = [ ('cash_on_delivery', 'Cash On Delivery'), ('online_payment', 'Online Payment')]

class InformatiiClient(models.Model):
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    email = models.EmailField()
    adresa = models.CharField(max_length=255)
    numar_telefon = models.CharField(max_length=15)
    payment_method = models.CharField(choices=PAYMENT_CHOICES, max_length=20)


class OrderItem(models.Model):
    customer = models.ForeignKey(InformatiiClient,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Reteta,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Customer : {self.customer} ; product : {self.product}'

    def get_cost(self):
        return self.price * self.quantity