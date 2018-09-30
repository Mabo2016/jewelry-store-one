from django.db import models
from django.urls import reverse
from datetime import date

from jewelryapp.models import Order
from jewelryapp.models import Jewelry

class OrderItem(models.Model):
    """Represents one or more jewelry items of the same type ordered by the user"""

    order = models.ForeignKey(
        Order,
        on_delete = models.CASCADE,
        null=True,
    )

    # This is done instead of duplicating the data of a jewelry item
    jewelry_item = models.ForeignKey(Jewelry, on_delete=models.CASCADE, null=True, blank=True,)

    count = models.IntegerField(default=1, editable=False, help_text="The number of jewelry items of the same type ordered")

    total_price = models.DecimalField(default=0, max_digits=8, decimal_places=2, editable=False, help_text="The total price of this type of item. It's count multiplied by its unit price")

    def __str__(self):
        """Identifies the object"""
        return f"{self.order.__str__()} {self.jewelry_item.__str__()} {self.id}"
