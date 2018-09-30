from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

class ShoppingCart(models.Model):
    """Keeps track of the items that the shopper wants to order"""

    shopper = models.OneToOneField(User, on_delete=models.CASCADE)

    total_price = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2,
        editable=False,
        help_text="The total price of all items in the shopping cart"
    )

    def __str__(self):
        """Identifies the object"""
        return f"{self.shopper.username} Shopping Cart"

    def get_absolute_url(self):
        """Returns url to this shopping cart for viewing and placing orders"""
        return reverse("shoppingcart_detail", args = [str(self.id)])

    @receiver(post_save, sender=User)
    def create_user_shoppingcart(sender, instance, created, **kwargs):
        if created:
            ShoppingCart.objects.create(shopper=instance)
        instance.shoppingcart.save()
