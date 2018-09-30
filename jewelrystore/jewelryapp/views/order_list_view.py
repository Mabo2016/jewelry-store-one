from django.views import generic

from jewelryapp.models import Order

class OrderListView(generic.ListView):
    model = Order
    paginate_by = 10
