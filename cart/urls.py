from django.urls import path

from .views import cart_add, cart_remove, cart_delete, CartView

app_name = 'cart'

urlpatterns = [
    path('', CartView.as_view(), name='cart_detail'),
    path('add/', cart_add, name='cart_add'),
    path('remove/<str:sku>', cart_remove, name='cart_remove'),
    path('clear/', cart_delete, name='cart_delete'),
]
