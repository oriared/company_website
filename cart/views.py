from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, F
from django.forms import formset_factory
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, View, DeleteView, UpdateView

from cart.models import Cart
from cart.forms import CartAddProductForm, BaseAddProductFormSet
from core.models import ProductPack


class CartView(LoginRequiredMixin, ListView):

    template_name = 'cart/cart.html'
    context_object_name = 'cart'

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


class CartAdd(LoginRequiredMixin, View):

    def post(self, request):

        FormSet = formset_factory(CartAddProductForm, formset=BaseAddProductFormSet)
        formset = FormSet(request.POST)

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


class CartUpdate(LoginRequiredMixin, UpdateView):

    fields = ('quantity',)
    slug_url_kwarg = 'sku'
    slug_field = 'pack__sku'

    success_url = reverse_lazy('cart:cart_detail')

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class CartRemove(LoginRequiredMixin, DeleteView):

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    slug_field = 'pack__sku'

    slug_url_kwarg = 'sku'
    success_url = reverse_lazy('cart:cart_detail')


# @login_required
# @require_POST
# def cart_update(request, sku):
#     form = CartUpdateProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         pack = ProductPack.objects.get(sku=sku)
#         Cart.objects.filter(user=request.user, pack=pack).\
#             update(quantity=cd.get('quantity'))

#     return redirect('cart:cart_detail')


# @login_required
# @require_POST
# def cart_remove(request, sku):
#     pack = ProductPack.objects.get(sku=sku)
#     cart = Cart.objects.filter(user=request.user, pack=pack)
#     cart.delete()

#     return redirect('cart:cart_detail')
