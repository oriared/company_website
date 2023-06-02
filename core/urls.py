from django.urls import path

from core.views import HomePageView, ProductsListView, ProductView, ProfileView

app_name = 'core'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('products/<slug:slug>/', ProductsListView.as_view(), name='products'),
    path('product/<slug:slug>/', ProductView.as_view(), name='product'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
