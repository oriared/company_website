from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from core.models import ProductPackaging
from .models import Order, OrderItem
from cart.cart import Cart


class OrderCreateView(CreateView):

    template_name = 'orders/order/create.html'
    model = Order
    fields = ('company', 'name', 'phone', 'email', 'city', 'comment')
    success_url = reverse_lazy('orders:created', kwargs={})

    def get_success_url(self):
        return reverse_lazy('orders:created', args=(self.object.uuid,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Оформление заказа'
        return context

    def form_valid(self, form):
        cart = Cart(self.request)
        self.object = form.save()
        for item in cart:
            OrderItem.objects.create(order=self.object,
                                     product_sku=ProductPackaging.objects.get(sku=item['packaging']),
                                     quantity=item['quantity'])
        cart.clear()
        return super().form_valid(form)


class CreatedOrderView(DetailView):

    template_name = 'orders/order/created_order.html'
    model = Order
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
