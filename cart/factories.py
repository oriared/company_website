from django.contrib.auth import get_user_model

import factory
from faker.factory import Factory

from cart.models import Cart
from core.factories import ProductPackagingFactory


factory_ru = Factory.create('ru-Ru')

User = get_user_model()


class CartFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Cart

    user = User.objects.create_user(username='test_user_38724',
                                    password='38462398568')
    product_sku = factory.SubFactory(ProductPackagingFactory)
    quantity = factory_ru.pyint(min_value=1, max_value=100)
