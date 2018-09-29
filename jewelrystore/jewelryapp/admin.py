from django.contrib import admin
from jewelryapp.models import Jewelry
from jewelryapp.models import CartItem
from jewelryapp.models import ShoppingCart

admin.site.register(Jewelry)
admin.site.register(CartItem)
admin.site.register(ShoppingCart)
