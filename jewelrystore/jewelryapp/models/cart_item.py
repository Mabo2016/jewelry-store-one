from django.db import models
from django.urls import reverse
from datetime import date

from jewelryapp.models import ShoppingCart
from jewelryapp.models import Jewelry

class CartItem(models.Model):
    """Represents a jewelry item added to the shopping cart by the shopper"""

    shopping_cart = models.ForeignKey(
        ShoppingCart,
        on_delete = models.CASCADE,
        null=True,
    )

    # This is done instead of duplicating the data of a jewelry item inside
    # a cart item.
    jewelry_item = models.ForeignKey(Jewelry, on_delete=models.CASCADE, null=True, blank=True)

    count = models.IntegerField(default=1, editable=False, help_text="The number of jewelry items of the same type added to the shopping cart")

    total_price = models.DecimalField(default=0, max_digits=8, decimal_places=2, editable=False, help_text="The total price of this type of item. It's count multiplied by its unit price")

    def __str__(self):
        """Identifies the object"""
        return f"{self.shopping_cart.__str__()} {self.jewelry_item.__str__()} {self.id}"

    # Decided against providing an url to this item.
    # It could be used to view this cart item in detail by accessing the
    # jewelry's data. And then provide the user with the ability to remove it
    # from cart. Instead a link to the jewelry item will be provided instead
    # to view it in detail, without any special functionality.
