from django.views import generic
from django.shortcuts import render

def list_cart_items(request):
    return render(request, 'jewelryapp/my_cart.html',)
