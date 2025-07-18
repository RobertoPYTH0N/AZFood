from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
# Create your views here.
from Mancare.models import Reteta
from .forms import FormularCumparatura
from cart.models import InformatiiClient, OrderItem
from .cart import Cart

def cart_view(request):
    cart = request.session.get('cart', {})
    products = [(Reteta.objects.get(id=prod_id), qty) for prod_id, qty in cart.items()]
    total = sum([prod.price * qty for prod, qty in products])
    form = FormularCumparatura()

    if request.method == 'POST':
        form = FormularCumparatura(request.POST)
        print( form,
              request.POST)
        if form.is_valid():
            print('Formularul este valid')
            cumparatura = form.save()
            print(cumparatura)
            print(cumparatura.pk)
        else:
             print('Formularul nu este valid')

        print(form.cleaned_data)

        
        payment_method = form.cleaned_data.get('payment_method')
        if payment_method == 'cash_on_delivery':
            return cash_on_delivery_view(request, cumparatura.pk)
        elif payment_method == 'online_payment':
            return online_payment_view (request, cumparatura.pk)
        

        
    return render(request, 'cart.html', {
        'products': products,
        'total': total,
        'form': form
    })

def cash_on_delivery_view(request, informatii_pk):
    cart = Cart(request)
    customer = get_object_or_404(InformatiiClient, pk = informatii_pk)
    for item, quantity in cart.products:
        OrderItem.objects.create(customer=customer,
                                 product=item,
                                 price=item.price,
                                 quantity=quantity)
    cart.empty()
    return render(request, 'comandaplasata.html')

def online_payment_view(request, informatii_pk):
    cart = Cart(request)
    customer = get_object_or_404(InformatiiClient, pk = informatii_pk)
    for item, quantity in cart.products:
        OrderItem.objects.create(customer=customer,
                                 product=item,
                                 price=item.price,
                                 quantity=quantity)
    cart.empty()
    return render(request, 'online_payment.html')

@require_POST
def add_to_cart_view(request, productid):
    print("add_to_cart_view")
    print("productid:", productid)
    print(request)
    print(request.POST)

    if not request.session.get('cart'):
        request.session['cart'] = {}

    quantity = request.session['cart'].get(productid, 0)
    request.session['cart'][productid] = quantity + int(request.POST.get('quantity', 0))

    print(request.session.get('cart'))

    request.session.modified = True
    cos_cumparaturi = request.session.get('cart')

    return redirect("cart_url")


@require_POST
def empty_cart_view(request):
    request.session['cart'] = {}
    return redirect("cart_url")
