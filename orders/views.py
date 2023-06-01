from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from cart.models import Cart
from core.models import ProductPack
from orders.models import Order, OrderItem
from orders.utils import send_order_email


class OrderCreateView(LoginRequiredMixin, CreateView):

    template_name = 'orders/order/create.html'
    model = Order
    fields = ('comment',)

    def get_success_url(self):
        return reverse_lazy('orders:created', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Оформление заказа'
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        for item in Cart.objects.filter(user=self.request.user):
            OrderItem.objects.create(order=self.object,
                                     pack=item.pack,
                                     quantity=item.quantity)
        send_order_email(order=self.object)
        Cart.objects.filter(user=self.request.user).delete()
        return super().form_valid(form)


class CreatedOrderView(LoginRequiredMixin, DetailView):

    template_name = 'orders/order/created_order.html'
    model = Order

    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object().user:
            return super().handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
