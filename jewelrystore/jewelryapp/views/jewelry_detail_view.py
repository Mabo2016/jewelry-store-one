from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F

from jewelryapp.models import Jewelry, CartItem, ShoppingCart

class JewelryDetailView(generic.DetailView):
    model = Jewelry

def add_to_cart(request, pk):
    jewelry = get_object_or_404(Jewelry, pk=pk)
    shopping_cart = request.user.shoppingcart
    # If this type of jewelry item already exists in the shopping cart then
    # do not create a new one, just increment its count in the cart item.
    cart_items = shopping_cart.cartitem_set.all()
    specific_cart_item = cart_items.filter(jewelry_item=jewelry)

    if specific_cart_item:
        specific_cart_item.update(count=F('count') + 1)
        specific_cart_item.update(total_price=F('total_price') + jewelry.price)
    else:
        new_cart_item = CartItem(
            shopping_cart=shopping_cart,
            jewelry_item=jewelry,
            total_price=jewelry.price,
        )
        new_cart_item.save()

    # Increment the total price for the shopping cart as a whole
    ShoppingCart.objects.filter(id=request.user.shoppingcart.id).update(total_price=F('total_price') + jewelry.price)

    return HttpResponseRedirect(reverse('jewelry_detail', args=(pk,)))
