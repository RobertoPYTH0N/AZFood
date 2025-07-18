from .cart import Cart

def cart_processor(request):
    cart = Cart(request)
    cart_count = len(cart)
    context = {
        "cart_count":cart_count,
        'products' : cart.products,
        'total':cart.total
    }
    return context