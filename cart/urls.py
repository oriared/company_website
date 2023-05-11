from django.urls import path

from .views import cart_add, cart_remove, CartView

app_name = 'cart'

urlpatterns = [
    path('', CartView.as_view(), name='cart_detail'),
    path('add/<str:product_vendor_code>/', cart_add, name='cart_add'),
    path('remove/<str:product_vendor_code>/', cart_remove, name='cart_remove'),
]
