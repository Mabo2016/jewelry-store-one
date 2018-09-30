from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Order(models.Model):
    """Keeps track of the items that the shopper ordered"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        help_text="The user that placed the order. I.e. The shopper.",
    )

    total_price = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2,
        editable=False,
        help_text="The total price of all items ordered by this order instance"
    )

    date_time_created = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when the order was placed"
    )

    def __str__(self):
        """Identifies the object"""
        return f"{self.user.username} Order No.{self.id}"

    def get_absolute_url(self):
        """Returns url to this order for checking"""
        return reverse("order_detail", args = [str(self.id)])
