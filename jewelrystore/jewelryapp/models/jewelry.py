from django.db import models
from django.urls import reverse
from datetime import date
from PIL import Image

class Jewelry(models.Model):
    """Fully describes a type or piece of jewelry to the user."""

    # Unique name of the jewelry. Typically identifies the metals used,
    # gem stones used, and some other special names.
    title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Required. E.g. Stainless Steel Mixed Color Pendant")

    date_time_added = models.DateField(auto_now = True)

    # AED's, UAE Dirhams
    price = models.DecimalField(max_digits=8, decimal_places=2)

    GEMSTONES = (
        ("n", "Not set"),
        ("r", "Ruby"),
        ("d", "Diamond"),
        ("s", "Saphire"),
        ("j", "Jade"),
        ("p", "Pearl"),
        ("a", "Amethyst"),
    )

    # Jewelry are differentiated by the jewels used and the metals used.
    # This variable is needed to clearly communicate the type of jewel used
    # in the jewelry item and thus communicate its value to the potential
    # customer.
    gemstones_used = models.CharField(
        max_length=1,
        choices=GEMSTONES,
        blank=True,
        default='n',
        help_text='Gemstones, like ruby or saphire, used in this item'
    )

    METALS = (
        ("n", "Not set"),
        ("n", "Common"),
        ("t", "Stainless Steel"),
        ("s", "Silver"),
        ("g", "Gold"),
        ("r", "Rose Gold"),
        ("p", "Platinum"),
    )

    # Jewelry are further differentiated by the type of metals they are made
    # from, not just the gem stones used. Silver, gold, or platinum all are
    # very important for jewelry.
    # This indicates what metals, if any, were used in the item, such as in
    # the handles or connectors.
    metallic_finish = models.CharField(
        max_length=1,
        choices=METALS,
        blank=True,
        default='n',
        help_text='Metal the jewelry is made from'
    )

    STATUS = (('o', 'Out of stock'), ('a', 'Available'),)

    availability = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='a',
        help_text='Availability for purchase'
    )

    # A small image that shows the jewelry for list views.
    thumbnail = models.ImageField(null=True, upload_to="jewelry-gallery")

    # A larger image of the jewelry item to show more detail for the customer.
    # Without null = True, django will complain about non-nullable field.
    detail_image = models.ImageField(null=True, upload_to="jewelry-gallery")

    def __str__(self):
        """Identifies the object"""
        return f"{self.title}"

    def get_absolute_url(self):
        """Returns url to detail page of the jewelry"""
        return reverse("jewelry_detail", args = [str(self.id)])
