from django.urls import path, include
from .views import *

urlpatterns = [path('', bun_venit, name ="acasa_url")]