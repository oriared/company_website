from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from core.models import ProductPackaging
from .cart import Cart
from .forms import build_add_form


@require_POST
def cart_add(request):
    cart = Cart(request)
    product_sku = request.POST.get('sku')
    package = get_object_or_404(ProductPackaging,
                                sku=product_sku)
    form = build_add_form(request.POST, product=package.product)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product_sku=product_sku,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, sku):
    cart = Cart(request)
    cart.remove(sku)
    return redirect('cart:cart_detail')


class CartView(TemplateView):

    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        context['title'] = 'Корзина'
        return context
