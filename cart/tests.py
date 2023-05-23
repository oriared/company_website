from django.contrib.sessions.backends.db import SessionStore
from django.http.request import HttpRequest
from django.test import TestCase

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

    def test_cart_remove(self):
        self.cart.add('abc123', 7)
        self.cart.remove('abc123')
        self.assertEqual(self.cart.cart, {})

    def test_cart_iter(self):
        p = ProductPackagingFactory()
        self.cart.add(p.sku, 3)
        for item in self.cart:
            assert item
