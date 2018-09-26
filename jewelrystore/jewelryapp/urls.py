from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index_view.index, name="index"),
    path('jewelry/', views.jewelry_list_view.JewelryListView.list_jewelry_filtered, name='jewelry'),
    path("jewelry/<int:pk>", views.jewelry_detail_view.JewelryDetailView.as_view(), name="jewelry_detail"),
    path("my_cart", views.my_cart_view.list_cart_items, name="my_cart"),
]
