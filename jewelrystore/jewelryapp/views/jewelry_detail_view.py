from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from jewelryapp.models import Jewelry
from jewelryapp.models import CartItem

class JewelryDetailView(generic.DetailView):
    model = Jewelry

def add_to_cart(request, pk):
    jewelry = get_object_or_404(Jewelry, pk=pk)
    new_cart_item = CartItem(
        shopping_cart=request.user.shoppingcart,
        jewelry_item=jewelry,
    )
    new_cart_item.save()
    return HttpResponseRedirect(reverse('jewelry_detail', args=(pk,)))
