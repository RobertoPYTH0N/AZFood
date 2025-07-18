
from django.urls import path
from .views import *

urlpatterns = [  
    path("", cart_view, name="cart_url"),
    path("add/<productid>", add_to_cart_view, name="add_to_cart_url"),
    path("empty", empty_cart_view, name="empty_cart_url"),
    path('comanda-plasata/', cash_on_delivery_view, name='cash_on_delivery_view'),
    path('online_payment/', online_payment_view, name='online_payment_view'),
]

