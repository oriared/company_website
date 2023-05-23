from django.urls import path

from .views import HomePageView, ProductsListView, ProductView

app_name = 'core'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('products/<slug:slug>/', ProductsListView.as_view(), name='products'),
    path('product/<slug:slug>/', ProductView.as_view(), name='product'),
]
