from django.urls import path

from .views import HomePageView, CategoryView, ProductView

app_name = 'core'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('products/<slug:slug>/', ProductView.as_view(), name='product'),
]