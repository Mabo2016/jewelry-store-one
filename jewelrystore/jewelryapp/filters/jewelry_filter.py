import django_filters
from datetime import date

from jewelryapp.models import Jewelry

class JewelryFilter(django_filters.FilterSet):
    """Filters jewelry search by category, price, and other attributes."""

    class Meta:
        model = Jewelry
        fields = {
            'title': ['contains'],
            'category': ['exact'],
            'gemstones_used': ['exact'],
            'metallic_finish': ['exact'],
            'date_time_added': ['exact', 'gt', 'lt'],
            'price': ['lt', 'gt'],
            'availability': ['exact'],
        }
