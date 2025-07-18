
from Mancare.models import Reteta

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = request.session.get('cart')
        if not request.session.get('cart'):
            cart = request.session['cart'] = {}
        self.cart = cart

    ## 1. Produsele
    @property
    def products(self):
        product_ids = self.cart.keys()
        cart_products =  Reteta.objects.filter(id__in=product_ids)
        return [(prod,  self.cart[str(prod.id)] )   for prod in cart_products ]

    
    ## 2. Lungimea
    def __len__(self):
        product_ids = self.cart.keys()
        cart_products =  Reteta.objects.filter(id__in=product_ids)
        return sum([(self.cart[str(prod.id)] )  for prod in cart_products ])

    ## 3. Adaugare Produse
    def add(self, productid, quantity):
        existing_quantity = self.cart.get(productid, 0)
        self.cart[productid] = quantity + existing_quantity  
        self.save()

    ## 4. Stergere cart
    def empty(self):
        self.cart = {}

    ### 5. Total cart
    @property
    def total(self):
        product_ids = self.cart.keys()
        cart_products =  Reteta.objects.filter(id__in=product_ids)
        return sum([(prod.price * self.cart[str(prod.id)] )   for prod in cart_products ])


    def save(self):
        self.session.modified = True
 


    def __int__(self):
        return 0
    
