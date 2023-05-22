import uuid

from django.db import models

from core.models import ProductPackaging


class Order(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4())
    company = models.CharField(max_length=100, verbose_name='Компания')
    name = models.CharField(max_length=50, verbose_name='ФИО')
    email = models.EmailField()
    phone = models.CharField(max_length=10, verbose_name='Телефон')
    city = models.CharField(max_length=100, verbose_name='Город')
    comment = models.TextField(max_length=1000, blank=True, verbose_name='Комментарий')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Изменён')

    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['-created'])]
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items',
                              on_delete=models.CASCADE)
    product_sku = models.ForeignKey(ProductPackaging, related_name='order_items',
                                    null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_weight(self):
        return self.product_sku.get_package_weight() * self.quantity

    def __str__(self):
        return str(self.id)
