import factory
from faker.factory import Factory

from cart.models import Cart
from core.factories import UserFactory, ProductPackagingFactory


factory_ru = Factory.create('ru-Ru')


class CartFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Cart

    user = factory.SubFactory(UserFactory)
    product_sku = factory.SubFactory(ProductPackagingFactory)
    quantity = factory_ru.pyint(min_value=1, max_value=100)
