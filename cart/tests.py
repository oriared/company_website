from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from cart.models import Cart
from core.factories import ProductPackagingFactory


User = get_user_model()


class CartViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='12345')
        self.client = Client()
        self.client.login(username='test_user', password='12345')
        self.packaging = ProductPackagingFactory()

    def test_cart_detail_view(self):
        response = self.client.get(reverse('cart:cart_detail'))
        self.assertEqual(response.status_code, 200)

    def test_cart_add_view(self):
        data = {'form-TOTAL_FORMS': ['3'], 'form-INITIAL_FORMS': ['3'],
                'form-MIN_NUM_FORMS': ['0'], 'form-MAX_NUM_FORMS': ['1000'],
                'form-0-quantity': [''], 'form-0-product_sku': ['123ABC'],
                'form-1-quantity': [''], 'form-1-product_sku': ['234FFF'],
                'form-2-quantity': ['3'], 'form-2-product_sku': [self.packaging.sku]}

        response = self.client.post(reverse('cart:cart_add'), data=data)

        c = Cart.objects.filter(user=self.user).first().product_sku.sku

        self.assertEqual(c, 'sku0')
        self.assertEqual(response.url, '/cart/')
