from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from core.models import ProductPackaging
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_vendor_code):
    cart = Cart(request)
    product = get_object_or_404(ProductPackaging,
                                vendor_code=product_vendor_code)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_vendor_code):
    cart = Cart(request)
    product = get_object_or_404(ProductPackaging,
                                vendor_code=product_vendor_code)
    cart.remove(product)
    return redirect('cart:cart_detail')


class CartView(TemplateView):

    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        context['title'] = 'Корзина'
        return context
