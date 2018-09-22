from django.views import generic

from jewelryapp.models import Jewelry

class JewelryDetailView(generic.DetailView):
    model = Jewelry
