from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index_view.index, name="index"),
    path('jewelry/', views.jewelry_list_view.JewelryListView.list_jewelry_filtered, name='jewelry'),
    path("jewelry/<int:pk>", views.jewelry_detail_view.JewelryDetailView.as_view(), name="jewelry_detail"),
    path("jewelry/add_to_cart/<int:pk>", views.jewelry_detail_view.add_to_cart, name="add_to_cart"),
    path("shoppingcart_detail/<int:pk>", views.shopping_cart_detail_view.ShoppingCartDetailView.as_view(), name="shoppingcart_detail"),
    path("shoppingcart_detail/clear_cart/<int:pk>", views.shopping_cart_detail_view.clear_cart, name="clear_cart"),
    path('orders/', views.order_list_view.OrderListView.as_view(), name='orders'),
    path("order/<int:pk>", views.order_detail_view.OrderDetailView.as_view(), name="order_detail"),
    path("order/place_order", views.shopping_cart_detail_view.place_order, name="place_order"),
]
