from django.urls import path

from core.views import HomePageView, ProductsListView, ProductView, ProfileView

app_name = 'core'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('category/<slug:slug>/', ProductsListView.as_view(), name='category'),
    path('product/<slug:slug>/', ProductView.as_view(), name='product'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
