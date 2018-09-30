from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.urls import reverse
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import F

from jewelryapp.models import ShoppingCart, Order, OrderItem

class ShoppingCartDetailView(generic.DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = ShoppingCart

def clear_cart(request, pk):
    """Resets the shopping cart so the past items do not
    interfere with future orders by the user"""

    request.user.shoppingcart.cartitem_set.all().delete()
    ShoppingCart.objects.filter(id=request.user.shoppingcart.id).update(total_price=0)

    return HttpResponseRedirect(reverse('shoppingcart_detail', args=(pk,)))

def place_order(request):
    """Helps users and the business keep track of the shopper's orders"""

    # Create a new order
    new_order = Order(user=request.user)
    new_order.save()
    new_order.refresh_from_db()

    # Used to compute the total price of all the ordered items
    # Needed to set the placed order's total price
    total_price = 0

    # Create new order items out of the cart items to populate the new order.
    cart_items = request.user.shoppingcart.cartitem_set.all()

    for item in cart_items:
        new_order_item = OrderItem(
            order=new_order,
            jewelry_item=item.jewelry_item,
            count=item.count,
            total_price=item.total_price,
        )
        new_order_item.save()
        total_price += item.total_price

    # The order's total price is not set automatically
    Order.objects.filter(id=new_order.id).update(total_price=F('total_price') + total_price)

    # Delete the shopping cart's contents. I.e. Clear it of its cart items.
    request.user.shoppingcart.cartitem_set.all().delete()

    return HttpResponseRedirect(reverse('order_detail', args=(new_order.id,)))
