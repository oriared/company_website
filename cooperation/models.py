from django.db import models
from .utils import path_upload_file


class Cooperation(models.Model):
    subject = models.CharField(max_length=30, verbose_name='Тема')
    company = models.CharField(max_length=100, verbose_name='Компания')
    person = models.CharField(max_length=100, verbose_name='ФИО')
    phone = models.CharField(max_length=11, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    city = models.CharField(max_length=50, blank=True, verbose_name='Город')
    text = models.TextField(verbose_name='Текст сообщения')
    file = models.FileField(upload_to=path_upload_file, blank=True,
                            verbose_name='Файл')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return f'{self.company}: {self.email}'

    class Meta:
        verbose_name = 'Запрос сотрудничества'
        verbose_name_plural = 'Запросы сотрудничества'
        ordering = ['-created']
