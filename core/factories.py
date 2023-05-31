import factory
from faker.factory import Factory

from core.models import (Product, ProductDetail, ProductPackaging,
                         ProductType, Category)


factory_ru = Factory.create('ru-Ru')


class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f"Категория {n}")
    slug = factory.Sequence(lambda n: f"categoryslug{n}")


class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductType

    name = factory.Sequence(lambda n: f"Тип {n}")
    slug = factory.Sequence(lambda n: f"typeslug{n}")
    category = factory.SubFactory(CategoryFactory)


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: f"Товар {n}")
    slug = factory.Sequence(lambda n: f"productslug{n}")
    type = factory.SubFactory(ProductTypeFactory)
    is_gost = factory_ru.boolean()
    is_published = True


class ProductDetailFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductDetail

    product = factory.SubFactory(ProductFactory)
    storage_time = factory_ru.pyint(max_value=24)
    storage_time_units = factory_ru.random_element(elements=('D', 'M'))
    calories = factory_ru.pyfloat(right_digits=1, positive=True,
                                  max_value=1000)
    proteins = factory_ru.pyfloat(right_digits=1, positive=True,
                                  max_value=50)
    fats = factory_ru.pyfloat(right_digits=1, positive=True,
                              max_value=50)
    carbohydrates = factory_ru.pyfloat(right_digits=1, positive=True,
                                       max_value=50)


class ProductPackagingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductPackaging

    product = factory.SubFactory(ProductFactory)
    sku = factory.Sequence(lambda n: f"sku{n}")
    weight = factory_ru.pyint(min_value=100, max_value=1500, step=10)
    packaging = factory_ru.pyint(min_value=10, max_value=40)
    price = factory_ru.pydecimal(left_digits=3, right_digits=2, positive=True)
