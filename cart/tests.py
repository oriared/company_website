from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from cart.factories import CartFactory
from cart.models import Cart
from core.factories import ProductPackFactory


User = get_user_model()


class CartViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='12345')
        self.client = Client()
        self.client.login(username='test_user', password='12345')
        self.pack = ProductPackFactory()

    def test_cart_detail_view(self):
        response = self.client.get(reverse('cart:cart_detail'))
        self.assertEqual(response.status_code, 200)

    def test_cart_add_view(self):
        data = {'form-TOTAL_FORMS': ['3'], 'form-INITIAL_FORMS': ['3'],
                'form-MIN_NUM_FORMS': ['0'], 'form-MAX_NUM_FORMS': ['1000'],
                'form-0-quantity': [''], 'form-0-sku': ['123ABC'],
                'form-1-quantity': [''], 'form-1-sku': ['234FFF'],
                'form-2-quantity': ['3'], 'form-2-sku': [self.pack.sku]}

        response = self.client.post(reverse('cart:cart_add'), data=data)

        sku = Cart.objects.filter(user=self.user).first().pack.sku

        self.assertEqual(response.status_code, 302)
        self.assertEqual(sku, 'sku0')
        self.assertEqual(response.url, '/cart/')

    def test_cart_update_view(self):

        cart = CartFactory(user=self.user)
        data = {'quantity': 150}

        response = self.client.post(reverse('cart:cart_update',
                                            kwargs={'sku': cart.pack.sku}),
                                    data=data)
        cart.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(cart.quantity, data.get('quantity'))

    def test_cart_remove_view(self):

        cart = CartFactory(user=self.user)

        response = self.client.post(reverse('cart:cart_remove',
                                            kwargs={'sku': cart.pack.sku}))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Cart.objects.count(), 0)
