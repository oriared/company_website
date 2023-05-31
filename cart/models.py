from django.contrib.auth import get_user_model
from django.db import models

from core.models import ProductPackaging
from .forms import CartUpdateProductForm

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User,
                             related_name='cart',
                             on_delete=models.CASCADE,
                             verbose_name='Клиент')
    product_sku = models.ForeignKey(ProductPackaging,
                                    related_name='cart',
                                    on_delete=models.PROTECT,
                                    verbose_name='Товар')
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    class Meta:
        ordering = ['product_sku__product__name']

    def get_total_weight(self):
        return self.product_sku.get_package_weight() * self.quantity

    def get_total_price(self):
        return self.product_sku.get_package_price() * self.quantity

    def get_update_form(self):
        form = CartUpdateProductForm({'quantity': self.quantity})
        return form
