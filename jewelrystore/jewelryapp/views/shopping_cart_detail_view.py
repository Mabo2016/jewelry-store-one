from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.urls import reverse
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from jewelryapp.models import ShoppingCart

class ShoppingCartDetailView(generic.DetailView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    model = ShoppingCart
