from django.urls import path

from cart.views import CartAdd, CartUpdate, CartRemove, CartView

app_name = 'cart'

urlpatterns = [
    path('', CartView.as_view(), name='cart_detail'),
    path('add/', CartAdd.as_view(), name='cart_add'),
    path('update/<str:sku>', CartUpdate.as_view(), name='cart_update'),
    path('remove/<str:sku>', CartRemove.as_view(), name='cart_remove'),
]
