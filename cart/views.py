from django.forms import formset_factory
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from .cart import Cart

from cart.forms import CartAddProductForm, BaseAddProductFormSet


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
def cart_remove(request, sku):
    cart = Cart(request)
    cart.remove(sku)
    return redirect('cart:cart_detail')


def cart_delete(request):
    cart = Cart(request)
    cart.clear()
    return redirect('core:home')


class CartView(TemplateView):

    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        # for item in context['cart']:
        #     item['update_quantity_form'] = CartUpdateQuantityForm(initial={
        #     'quantity': item['quantity'],
        #     'override': True})

        context['title'] = 'Корзина'
        return context
