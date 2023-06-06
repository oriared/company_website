from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import F, Sum
from django.urls import reverse

from core.models import ProductPack


User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User,
                             verbose_name='Клиент',
                             related_name='order',
                             on_delete=models.CASCADE)
    comment = models.TextField('Комментарий', max_length=1000, blank=True)
    created = models.DateTimeField('Создан', auto_now_add=True)
    updated = models.DateTimeField('Изменён', auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        return f'Заказ {self.id}'

    def get_absolute_url(self) -> str:
        return reverse('orders:created', kwargs={'pk': self.pk})

    def get_order_price(self) -> Decimal:
        op = self.items.annotate(op=F('pack__price')
                                 * F('pack__items_in_box')
                                 * F('quantity')).aggregate(Sum('op')).get('op__sum')
        return op.quantize(Decimal('1.00'))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name='Заказ', related_name='items',
                              on_delete=models.CASCADE)
    pack = models.ForeignKey(ProductPack, verbose_name='Фасовка',
                             related_name='order_item', null=True,
                             on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField('Количество', default=1)

    class Meta():
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_total_weight(self) -> int:
        return self.pack.get_package_weight() * self.quantity

    def get_total_price(self) -> Decimal:
        tp = self.pack.get_package_price() * self.quantity
        return tp.quantize(Decimal('1.00'))

    def __str__(self) -> str:
        return str(self.id)
