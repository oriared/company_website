from django.test import TestCase
from django.urls import reverse

from core.factories import CategoryFactory, ProductFactory
from core.models import Category


class HomePageTest(TestCase):
    def setUp(self):
        for _ in range(10):
            CategoryFactory()

    def test_home_page_view(self):
        response = self.client.get(reverse('core:home'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(tuple(response.context['categories']),
                         tuple(Category.published.all()))


class CategoryTest(TestCase):
    def setUp(self):
        self.product = ProductFactory()
        self.category = self.product.type.category

    def test_category_view(self):
        response = self.client.get(reverse('core:category',
                                           kwargs={'slug': self.category.slug}))

        self.assertEqual(response.status_code, 200)

    def test_category_get_absolute_url(self):
        response = self.client.get(self.category.get_absolute_url())

        self.assertEqual(response.context['products'].first().type.category,
                         self.category)


class ProductTest(TestCase):
    def setUp(self):
        self.product = ProductFactory()

    def test_product_view(self):
        response = self.client.get(reverse('core:product',
                                           kwargs={'slug': self.product.slug}))

        self.assertEqual(response.status_code, 200)

    def test_product_get_absolute_url(self):
        response = self.client.get(self.product.get_absolute_url())

        self.assertEqual(response.context['object'], self.product)
