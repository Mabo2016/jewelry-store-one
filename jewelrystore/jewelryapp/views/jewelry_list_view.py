from django.views import generic

from jewelryapp.models import Jewelry

class JewelryListView(generic.ListView):
    model = Jewelry
    paginate_by = 10
