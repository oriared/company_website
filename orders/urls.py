from django.urls import path

from orders.views import OrderCreateView, CreatedOrderView, OrderListView

app_name = 'orders'

urlpatterns = [
    path('list', OrderListView.as_view(), name='orders_list'),
    path('create', OrderCreateView.as_view(), name='create'),
    path('created/<int:pk>', CreatedOrderView.as_view(), name='created'),
]
