# Generated by Django 4.2.1 on 2023-05-30 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['product_sku__product__name']},
        ),
    ]
