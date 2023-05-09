# Generated by Django 4.2.1 on 2023-05-07 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_category_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nutriens',
            options={'ordering': ['pk'], 'verbose_name': 'КБЖУ', 'verbose_name_plural': 'КБЖУ'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='nutriens',
        ),
        migrations.AddField(
            model_name='nutriens',
            name='product',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.product', verbose_name='Товар'),
        ),
    ]
