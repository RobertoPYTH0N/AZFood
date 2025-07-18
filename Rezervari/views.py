from django.shortcuts import render
from .forms import FormularRezervare

def obtine_rezervare(request):
    form = FormularRezervare() 
    return render(request, 'rezervari.html', {'form': form})

def confirmare_rezervare(request):
    if request.method == 'POST':
        form = FormularRezervare(request.POST)
        if form.is_valid():
            form.save()
            print("se salveaza...?")
    return render(request, 'confirmarerezervare.html')