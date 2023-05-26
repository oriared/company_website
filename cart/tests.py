from django.contrib.sessions.backends.db import SessionStore
from django.http.request import HttpRequest
from django.test import TestCase
from django.urls import reverse

from core.factories import ProductPackagingFactory
from .cart import Cart


class CartTest(TestCase):
    def setUp(self):
        self.request = HttpRequest
        self.request.session = SessionStore()
        self.request.session.create()
        self.cart = Cart(self.request)

    def test_cart_add(self):
        self.cart.add('abc123', 7)
        self.assertEqual(self.cart.cart['abc123'].get('quantity'), 7)

    def test_cart_update(self):
        self.cart.add('abc123', 7)
        self.cart.update('abc123', 2)
        self.assertEqual(self.cart.cart['abc123'].get('quantity'), 2)

    def test_cart_remove(self):
        self.cart.add('abc123', 7)
        self.cart.remove('abc123')
        self.assertEqual(self.cart.cart, {})

    def test_cart_iter(self):
        p = ProductPackagingFactory()
        self.cart.add(p.sku, 3)
        for item in self.cart:
            assert item


class CartViewsTest(TestCase):
    def setUp(self):
        pass

    def test_cart_detail_view(self):
        response = self.client.get(reverse('cart:cart_detail'))
        self.assertEqual(response.status_code, 200)

    def test_cart_add_view(self):
        data = {'form-TOTAL_FORMS': ['3'], 'form-INITIAL_FORMS': ['3'],
                'form-MIN_NUM_FORMS': ['0'], 'form-MAX_NUM_FORMS': ['1000'],
                'form-0-quantity': [''], 'form-0-product_sku': ['123ABC'],
                'form-1-quantity': ['2'], 'form-1-product_sku': ['234FFF'],
                'form-2-quantity': ['3'], 'form-2-product_sku': ['000AAA']}
        response = self.client.post(reverse('cart:cart_add'), data=data)
        self.assertEqual(response.url, '/cart/')
