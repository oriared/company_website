from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from .models import Product, Category, Carousel


class HomePageView(TemplateView):

    template_name = 'core/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['categories'] = Category.objects.filter(is_published=True)
        context['carousel'] = Carousel.objects.filter(is_active=True)
        context['news'] = []
        return context


class CategoryView(ListView):

    template_name = 'core/category.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(is_published=True, type__category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs.get('slug')).name
        return context


class ProductView(DetailView):

    template_name = 'core/product.html'

    def get_queryset(self):
        return Product.objects.filter(is_published=True).select_related('productdetail')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Product.objects.get(slug=self.kwargs.get('slug')).name
        return context
