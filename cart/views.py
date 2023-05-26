from django.forms import formset_factory
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from .cart import Cart

from cart.forms import (CartAddProductForm,
                        CartUpdateProductForm,
                        BaseAddProductFormSet)


@require_POST
def cart_add(request):
    cart = Cart(request)

    ProductFormSet = formset_factory(CartAddProductForm,
                                     formset=BaseAddProductFormSet)
    formset = ProductFormSet(request.POST)
    if formset.is_valid():
        cd = formset.cleaned_data
        for item in cd:
            if item.get('quantity'):
                cart.add(product_sku=item.get('product_sku'),
                         quantity=item.get('quantity'))
    return redirect('cart:cart_detail')


@require_POST
def cart_update(request):
    cart = Cart(request)
    form = CartUpdateProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.update(product_sku=cd.get('product_sku'),
                    quantity=cd.get('quantity'))
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
        context['title'] = 'Корзина'
        cart = Cart(self.request)
        for item in cart:
            item['update_quantity_form'] = CartUpdateProductForm(
                initial={
                 'quantity': item['quantity'],
                 'product_sku': item['packaging'].sku
                 }
                 )

        return context
