from django.views import generic
from django.shortcuts import render

from jewelryapp.models import Jewelry
from jewelryapp.filters import JewelryFilter

class JewelryListView(generic.ListView):
    model = Jewelry
    paginate_by = 10

    def list_jewelry_filtered(request):
        sorting_attr="date_time_added"
        jewelry_filter = JewelryFilter(request.GET, queryset=Jewelry.objects.all())
        return render(
            request,
            'jewelryapp/jewelry_list.html',
            {'filter': jewelry_filter, 'sorting_attr': sorting_attr,}
        )
