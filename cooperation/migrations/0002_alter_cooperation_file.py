# Generated by Django 4.2.1 on 2023-05-16 16:32

import cooperation.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperation',
            name='file',
            field=models.FileField(blank=True, upload_to=cooperation.utils.path_upload_file, verbose_name='Файл'),
        ),
    ]
