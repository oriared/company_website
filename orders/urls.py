from django.urls import path

from orders.views import OrderCreateView, CreatedOrderView

app_name = 'orders'

urlpatterns = [
    path('create', OrderCreateView.as_view(), name='create'),
    path('created/<int:pk>', CreatedOrderView.as_view(), name='created'),
]
