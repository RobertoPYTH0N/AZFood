from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Reteta, categorie

from cart.forms import AddToCartForm
from cart.cart import  Cart

# Create your views here.

def lista_cu_categorii(request):
    categorii = categorie.objects.all()
    retete = Reteta.objects.all()
    context = {'categorie':categorii, 'retete': retete} 
    return render(request, "meniu.html", context) 

def detalii_reteta(request, slug):
    retete = Reteta.objects.filter(slug=slug).first()
    add_to_cart_form = AddToCartForm()
    context = {'Reteta': retete, 'add_form': add_to_cart_form}
    return render(request, "detalii_reteta.html", context)

def cookie_view(request):
    print(request.COOKIES.get('prajitura'))
    
    response =  HttpResponse("Aici se va seta un cookie")

    return response


def session_view(request):
    print(request.session.get("cafea"))
    response =  HttpResponse("Aici ne uitam de sesiune")
    return response 

from rest_framework import generics
from .serializers import RetetaSerializer

class RetetaListView(generics.ListAPIView):
    queryset = Reteta.objects.all()
    serializer_class = RetetaSerializer

class RetetaDetailView(generics.RetrieveAPIView):
    queryset = Reteta.objects.all()
    serializer_class = RetetaSerializer

class RetetaCreateView(generics.CreateAPIView):
    queryset = Reteta.objects.all()
    serializer_class = RetetaSerializer

