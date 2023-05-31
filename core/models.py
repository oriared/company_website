from django.db import models
from django.urls import reverse

from core.utils import path_category_image, path_product_image


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class Product(models.Model):
    name = models.CharField('Наименование', max_length=255)
    slug = models.SlugField('URL', max_length=255, unique=True)
    type = models.ForeignKey('ProductType', verbose_name='Тип',
                             on_delete=models.PROTECT)
    image = models.ImageField('Фото', upload_to=path_product_image,
                              default='images/default.jpg')
    is_gost = models.BooleanField('Соответствует ГОСТ')
    is_published = models.BooleanField('Доступен', default=True)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self) -> str:
        return reverse('core:product', kwargs={'slug': self.slug})

    def display_category(self) -> str:
        return self.type.category

    display_category.short_description = 'Категория'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)


class ProductDetail(models.Model):
    CHOICES = (
        ('DAYS', 'дней'),
        ('MOUNTHS', 'мес')
    )

    product = models.OneToOneField('Product', verbose_name='Товар',
                                   null=True, on_delete=models.SET_NULL)
    description = models.TextField('Описание', blank=True)
    conditions = models.TextField('Условия хранения', blank=True)
    storage_time = models.PositiveIntegerField('Срок хранения')
    storage_time_units = models.CharField('', max_length=7, choices=CHOICES,
                                          default='MOUNTHS')
    calories = models.FloatField('Калорийность')
    proteins = models.FloatField('Белки')
    fats = models.FloatField('Жиры')
    carbohydrates = models.FloatField('Углеводы')

    class Meta:
        verbose_name = 'Характеристики товара'
        verbose_name_plural = 'Характеристики товара'


class ProductPackaging(models.Model):
    product = models.ForeignKey('Product', verbose_name='Товар',
                                null=True,
                                on_delete=models.CASCADE,
                                related_name='packaging')
    sku = models.CharField('Артикул', max_length=50, unique=True)
    weight = models.PositiveIntegerField('Вес, грамм')
    packaging = models.PositiveIntegerField('Вложение, шт')
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2)

    def __str__(self):
        return self.sku

    def get_package_weight(self) -> int:
        return self.weight * self.packaging

    def get_package_price(self) -> float:
        return self.price * self.packaging

    class Meta:
        verbose_name = 'Фасовка'
        verbose_name_plural = 'Фасовка'


class ProductType(models.Model):
    name = models.CharField('Категория', max_length=100, db_index=True)
    slug = models.SlugField('URL', max_length=255, unique=True)
    category = models.ForeignKey('Category', verbose_name='Категория',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товаров'
        ordering = ('name',)


class Category(models.Model):
    name = models.CharField('Категория', max_length=100)
    slug = models.SlugField('URL', max_length=255, unique=True)
    image = models.ImageField('Фото', upload_to=path_category_image,
                              default='images/default.jpg')
    is_published = models.BooleanField('Видимость', default=True)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self) -> str:
        return reverse('core:products', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Carousel(models.Model):
    description = models.CharField('Описание', max_length=100)
    image = models.ImageField('Изображение', upload_to='images/carousel/')
    is_published = models.BooleanField('Видимость', default=True)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = 'Карусель'
        verbose_name_plural = 'Карусель'
