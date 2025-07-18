from django.contrib import admin
from .models import InformatiiClient, OrderItem

# Register your models here.

@admin.register(InformatiiClient)
class CoscumparaturiAdmin(admin.ModelAdmin):
    list_display = ('nume', 'prenume', 'email', 'numar_telefon', 'adresa', 'payment_method')
    search_fields = ('nume', 'prenume', 'email', 'numar_telefon', 'payment_method')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'price', 'quantity')
    search_fields = ('customer', 'product', 'price', 'quantity')
