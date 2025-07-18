from django.urls import path
from .views import *

urlpatterns=[
     path('', lista_cu_categorii, name="Mancare_url"),
     path("api/products/", RetetaListView.as_view()),
     path("api/products/details/<pk>/", RetetaDetailView.as_view()),
     path("api/products/create/", RetetaCreateView.as_view()),
     path("cookie/", cookie_view),
     path("session/", session_view),
     path("<slug>", detalii_reteta),
]