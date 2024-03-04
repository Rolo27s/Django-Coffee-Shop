from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-to-cart/<int:coffee_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart-list/', views.cart_list, name='cart_list'),
    path('remove-from-cart/<int:cartlist_id>/', views.remove_from_cart, name='remove_from_cart'),
]