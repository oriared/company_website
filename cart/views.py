from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView

from cart.models import Cart
from cart.forms import CartAddProductForm, CartUpdateProductForm, BaseAddProductFormSet
from core.models import ProductPackaging


@login_required
@require_POST
def cart_add(request):
    ProductFormSet = formset_factory(CartAddProductForm,
                                     formset=BaseAddProductFormSet)
    formset = ProductFormSet(request.POST)
    if formset.is_valid():
        cd = formset.cleaned_data
        for item in cd:
            if item.get('quantity'):
                product_sku = ProductPackaging.objects.get(sku=item.get('product_sku'))
                cart, _ = Cart.objects.get_or_create(user=request.user,
                                                     product_sku=product_sku,
                                                     defaults={'quantity': 0})
                cart.quantity += item.get('quantity')
                cart.save()

    return redirect('cart:cart_detail')


@login_required
@require_POST
def cart_update(request, sku):
    form = CartUpdateProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        product_sku = ProductPackaging.objects.get(sku=sku)
        Cart.objects.filter(user=request.user, product_sku=product_sku).\
            update(quantity=cd.get('quantity'))

    return redirect('cart:cart_detail')


@login_required
@require_POST
def cart_remove(request, sku):
    product_sku = ProductPackaging.objects.get(sku=sku)
    cart = Cart.objects.filter(user=request.user, product_sku=product_sku)
    cart.delete()

    return redirect('cart:cart_detail')


class CartView(LoginRequiredMixin, ListView):

    template_name = 'cart/cart.html'

    def get_queryset(self):
        user_cart = Cart.objects.filter(user=self.request.user)
        return user_cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_price = sum([item.get_total_price() for item in self.object_list])
        context['total_price'] = total_price
        context['title'] = 'Корзина'
        return context
