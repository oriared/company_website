from django.urls import path

from .views import OrderCreateView, CreatedOrderView

app_name = 'orders'

urlpatterns = [
    path('create', OrderCreateView.as_view(), name='create'),
    path('created/<uuid:uuid>', CreatedOrderView.as_view(), name='created'),
]
