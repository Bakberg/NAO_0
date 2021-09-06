from django.db import models
from django import forms


class Coment (models.Model):
    title = models.CharField(max_length=25, blank=True, verbose_name='Имя')
    task = models.TextField(blank=True, verbose_name='Вопрос')
    is_published = models.BooleanField(default=False, verbose_name='Публирован')
    number = models.CharField(max_length=12, verbose_name='Номер отправителя')
    otvet = models.TextField(blank=True, verbose_name='Ответ')

    class Meta:
        verbose_name = 'Вопрос-ответь'
        verbose_name_plural = 'Вопрос-ответь'

    def __str__(self):
        return self.title