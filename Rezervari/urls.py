from django.urls import path
from .views import *

urlpatterns = [
     path('', obtine_rezervare),
     path('confirmare-rezervare', confirmare_rezervare),
]