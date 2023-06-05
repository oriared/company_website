from django.contrib.auth import get_user_model

import factory
from faker.factory import Factory

from orders.models import Order, OrderItem
from core.factories import ProductPackFactory


factory_ru = Factory.create('ru-Ru')

User = get_user_model()


class OrderFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Order

    user = User.objects.get(username='test_user')
    comment = factory_ru.sentence(nb_words=12)


class OrderItemFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = OrderItem

    order = factory.SubFactory(OrderFactory)
    pack = factory.SubFactory(ProductPackFactory)
    quantity = factory_ru.pyint(min_value=1, max_value=100)
