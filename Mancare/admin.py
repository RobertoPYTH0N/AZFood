from django.contrib import admin

# Register your models here.

from .models import Reteta, categorie

@admin.register(categorie)
class AdminCategory(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Reteta)
class AdminReteta(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "price", "category")
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("price",)