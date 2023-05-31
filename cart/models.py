from django.contrib.auth import get_user_model
from django.db import models

from core.models import ProductPackaging
from cart.forms import CartUpdateProductForm

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User,
                             verbose_name='Клиент',
                             related_name='cart',
                             on_delete=models.CASCADE)
    product_sku = models.ForeignKey(ProductPackaging,
                                    verbose_name='Товар',
                                    related_name='cart',
                                    on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField('Количество')

    class Meta:
        ordering = ['product_sku__product__name']

    def get_total_weight(self) -> int:
        return self.product_sku.get_package_weight() * self.quantity

    def get_total_price(self) -> float:
        return self.product_sku.get_package_price() * self.quantity

    def get_update_form(self) -> CartUpdateProductForm:
        form = CartUpdateProductForm({'quantity': self.quantity})
        return form
