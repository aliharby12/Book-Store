from django.urls import path

from project.store.views import decrease_cart_item, increase_cart_item, cart_detail

urlpatterns = [
    path('', cart_detail, name='cart-detail'),
    path('increase-cart-item/<int:pk>/', increase_cart_item, name='increase-cart-item'),
    path('decrease-cart-item/<int:pk>/', decrease_cart_item, name='decrease-cart-item'),
]