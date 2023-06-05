from django.contrib.auth import get_user_model
from django.forms import formset_factory
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView

from core.models import Product, Category, Carousel
from cart.forms import CartAddProductForm, BaseAddProductFormSet


User = get_user_model()


class HomePageView(TemplateView):

    template_name = 'core/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        context['carousel'] = Carousel.published.all()
        return context


class ProductsListView(ListView):

    template_name = 'core/category.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.published.filter(type__category__slug=self.kwargs['slug'])\
            .select_related('type__category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.published.get(slug=self.kwargs['slug']).name
        context['current_cat'] = self.kwargs['slug']
        return context


class ProductView(DetailView):

    template_name = 'core/product.html'

    def get_queryset(self):
        return Product.published.select_related('productdetail')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            ProductFormSet = formset_factory(CartAddProductForm,
                                             formset=BaseAddProductFormSet,
                                             extra=0)
            packs = self.object.pack.filter(is_published=True)
            initial = tuple(packs.values('sku'))
            formset = ProductFormSet(initial=initial)
            context['cart_add_formset_with_packs'] = zip(packs, formset)
            context['management_form'] = formset.management_form
        context['title'] = self.object.name
        return context


class ProfileView(TemplateView):

    template_name = 'core/profile.html'
    slug_field = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
