# Generated by Django 4.2.1 on 2023-06-05 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperation', '0003_rename_person_cooperation_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperation',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Контактное лицо'),
        ),
    ]
