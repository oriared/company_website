# Generated by Django 4.2.1 on 2023-06-06 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_producttype_name'),
        ('orders', '0006_remove_order_orders_orde_created_743fca_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='pack',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='order_item', to='core.productpack', verbose_name='Фасовка'),
        ),
    ]
