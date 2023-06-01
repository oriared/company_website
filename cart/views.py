from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, F
from django.forms import formset_factory
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView

from cart.models import Cart
from cart.forms import CartAddProductForm, CartUpdateProductForm, BaseAddProductFormSet
from core.models import ProductPack


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
                pack = ProductPack.objects.get(sku=item.get('sku'))
                cart, _ = Cart.objects.get_or_create(user=request.user,
                                                     pack=pack,
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
        pack = ProductPack.objects.get(sku=sku)
        Cart.objects.filter(user=request.user, pack=pack).\
            update(quantity=cd.get('quantity'))

    return redirect('cart:cart_detail')


@login_required
@require_POST
def cart_remove(request, sku):
    pack = ProductPack.objects.get(sku=sku)
    cart = Cart.objects.filter(user=request.user, pack=pack)
    cart.delete()

    return redirect('cart:cart_detail')


class CartView(LoginRequiredMixin, ListView):

    template_name = 'cart/cart.html'

    def get_queryset(self):
        user_cart = Cart.objects.filter(user=self.request.user).\
            select_related('pack__product')
        return user_cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # total_price = sum([item.get_total_price() for item in self.object_list])
        total_price = self.object_list.aggregate(tp=Sum(F('quantity') *
                                                        F('pack__price') *
                                                        F('pack__items_in_box'))).\
            get('tp')

        context['total_price'] = total_price
        context['title'] = 'Корзина'
        return context
