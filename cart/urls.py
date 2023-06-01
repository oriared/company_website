from django.urls import path

from cart.views import CartAddView, cart_update, cart_remove, CartView

app_name = 'cart'

urlpatterns = [
    path('', CartView.as_view(), name='cart_detail'),
    path('add/', CartAddView.as_view(), name='cart_add'),
    path('update/<str:sku>', cart_update, name='cart_update'),
    path('remove/<str:sku>', cart_remove, name='cart_remove'),
]
