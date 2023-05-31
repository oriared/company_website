from django.contrib.auth import get_user_model
from django.db import models

from core.models import ProductPackaging

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User,
                             related_name='order',
                             on_delete=models.CASCADE,
                             verbose_name='Клиент')
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

    class Meta():
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_total_weight(self):
        return self.product_sku.get_package_weight() * self.quantity

    def __str__(self):
        return str(self.id)
