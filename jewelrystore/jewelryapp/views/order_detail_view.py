from django.views import generic

from jewelryapp.models import Order
from jewelryapp.models import OrderItem

class OrderDetailView(generic.DetailView):
    model = Order
