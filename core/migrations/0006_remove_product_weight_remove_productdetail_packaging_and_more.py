# Generated by Django 4.2.1 on 2023-05-10 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_carousel_options_remove_carousel_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='packaging',
        ),
        migrations.RemoveField(
            model_name='productdetail',
            name='vendor_code',
        ),
        migrations.CreateModel(
            name='ProductPackaging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_code', models.CharField(blank=True, max_length=50, verbose_name='Артикул')),
                ('weight', models.PositiveIntegerField(verbose_name='Вес, грамм')),
                ('packaging', models.CharField(max_length=255, verbose_name='Вложение, шт')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.product', verbose_name='Товар')),
            ],
        ),
    ]
