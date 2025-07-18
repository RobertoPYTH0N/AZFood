from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bun_venit(request):
    return render(request, "acasa.html")
