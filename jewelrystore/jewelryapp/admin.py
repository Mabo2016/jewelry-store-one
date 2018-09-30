from django.contrib import admin
from jewelryapp.models import Jewelry, CartItem, ShoppingCart, Order, OrderItem

admin.site.register(Jewelry)
admin.site.register(CartItem)
admin.site.register(ShoppingCart)
admin.site.register(Order)
admin.site.register(OrderItem)
