from django.db import models
from cooperation.utils import path_upload_file


class Cooperation(models.Model):
    subject = models.CharField('Тема', max_length=30)
    company = models.CharField('Компания', max_length=100)
    person = models.CharField('ФИО', max_length=100)
    phone = models.CharField('Телефон', max_length=11)
    email = models.EmailField('Email')
    city = models.CharField('Город', max_length=50, blank=True)
    text = models.TextField('Текст сообщения')
    file = models.FileField('Файл', upload_to=path_upload_file, blank=True)
    created = models.DateTimeField('Дата', auto_now_add=True)

    def __str__(self):
        return f'{self.company}: {self.email}'

    class Meta:
        verbose_name = 'Запрос сотрудничества'
        verbose_name_plural = 'Запросы сотрудничества'
        ordering = ['-created']
