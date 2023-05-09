from django.db import models
from django.urls import reverse

from .utils import path_category_image, path_product_image


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name='URL')
    type = models.ForeignKey('ProductType', on_delete=models.PROTECT,
                             verbose_name='Тип')
    image = models.ImageField(upload_to=path_product_image,
                              default='images/default.jpg',
                              verbose_name='Фото')
    weight = models.PositiveIntegerField(verbose_name='Вес, грамм')
    is_gost = models.BooleanField(verbose_name='Произведён по ГОСТ')
    is_post = models.BooleanField(verbose_name='Постный продукт')
    is_published = models.BooleanField(default=True, verbose_name='Виден всем')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', args=(self.slug,))

    def display_category(self):
        return self.type.category

    display_category.short_description = 'Категория'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']
        indexes = [models.Index(fields=['slug'])]


class ProductDetail(models.Model):
    product = models.OneToOneField('Product', on_delete=models.CASCADE,
                                   null=True, verbose_name="Товар")
    description = models.TextField(default='Описание отсутствует',
                                   verbose_name='Описание')
    vendor_code = models.CharField(max_length=50, blank=True,
                                   verbose_name='Артикул')
    conditions = models.TextField(blank=True, verbose_name='Условия хранения')
    packaging = models.CharField(max_length=255, verbose_name='Фасовка')
    calories = models.FloatField(verbose_name='Калорийность')
    proteins = models.FloatField(verbose_name='Белки')
    fats = models.FloatField(verbose_name='Жиры')
    carbohydrates = models.FloatField(verbose_name='Углеводы')

    def get_packing_weights(self):
        packing = tuple(map(int, self.packaging.split(', ')))
        return packing

    class Meta:
        verbose_name = 'Характеристики товара'
        verbose_name_plural = 'Характеристики товара'


class ProductType(models.Model):
    name = models.CharField(max_length=100, db_index=True,
                            verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True,
                            verbose_name='URL')
    category = models.ForeignKey('Category', on_delete=models.CASCADE,
                                 verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товаров'
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True,
                            verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='URL')
    image = models.ImageField(upload_to=path_category_image,
                              default='images/default.jpg',
                              verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Виден всем')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog', args=(self.slug,))

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Carousel(models.Model):
    description = models.CharField(max_length=100, verbose_name='Описание')
    image = models.ImageField(upload_to='images/carousel/', 
                              verbose_name='Изображение')
    is_active = models.BooleanField(default=True, verbose_name='Виден всем')

    class Meta:
        verbose_name = 'Карусель'
        verbose_name_plural = 'Карусель'
