# Generated by Django 4.2.1 on 2023-06-05 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_productpack_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttype',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Тип'),
        ),
    ]
