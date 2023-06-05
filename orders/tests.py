from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from cart.factories import CartFactory
from orders.models import Order
from orders.factories import OrderFactory, OrderItemFactory


User = get_user_model()


class OrderViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='12345')
        self.client = Client()
        self.client.login(username='test_user', password='12345')
        self.quantities = (3, 11, 45)
        for i in self.quantities:
            CartFactory(user=self.user, quantity=i)

    def test_order_create(self):
        data = {'comment': 'qwerty qwerty'}
        response = self.client.post(reverse('orders:create'), data=data)
        ord = Order.objects.get(pk=1)

        order_items_quantities = tuple(item['quantity']
                                       for item in ord.items.values('quantity'))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(ord.comment, data.get('comment'))
        self.assertEqual(order_items_quantities, self.quantities)

    def test_created_order(self):
        order = OrderFactory(user=self.user)
        OrderItemFactory(order=order)

        response = self.client.get(reverse('orders:created', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, 200)

    def test_orders_list(self):
        response = self.client.get(reverse('orders:orders_list'))

        self.assertEqual(response.status_code, 200)
