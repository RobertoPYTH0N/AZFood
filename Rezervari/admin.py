from django.contrib import admin
from .models import Rezervare

@admin.register(Rezervare)
class RezervareAdmin(admin.ModelAdmin):
    list_display = ('nume', 'prenume', 'data', 'ora', 'email_sau_telefon')
    search_fields = ('nume', 'prenume', 'email_sau_telefon')