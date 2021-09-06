from django.db import models
from django import forms


class Dropdown_one (models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    task = models.TextField(blank=True, verbose_name='Описание')
    datab = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    datas = models.DateTimeField(auto_now=True, verbose_name='Дата последного добавления')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фотография')
    is_pblished = models.BooleanField(default=True, verbose_name='Публирован')
    book = models.FileField(upload_to='static/%Y/%m/%d', blank=True, verbose_name='PDF книги')

    class Meta:
        verbose_name = 'Образование категорий'
        verbose_name_plural = 'Образование категорий'

    def __str__(self):
        return self.title

class Dropdown_two (models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    task = models.TextField(blank=True, verbose_name='Описание')
    datab = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    datas = models.DateTimeField(auto_now=True, verbose_name='Дата последного добавления')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фотография')
    is_pblished = models.BooleanField(default=True, verbose_name='Публирован')
    book = models.FileField(upload_to='static/%Y/%m/%d', blank=True, verbose_name='PDF книги')

    class Meta:
        verbose_name = 'Наука категорий'
        verbose_name_plural = 'Наука категорий'

    def __str__(self):
        return self.title

class Dropdown_three (models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    task = models.TextField(blank=True, verbose_name='Описание')
    datab = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    datas = models.DateTimeField(auto_now=True, verbose_name='Дата последного добавления')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фотография')
    is_pblished = models.BooleanField(default=True, verbose_name='Публирован')
    book = models.FileField(upload_to='static/%Y/%m/%d', blank=True, verbose_name='PDF книги')

    class Meta:
        verbose_name = 'Методология категорий'
        verbose_name_plural = 'Методология категорий'

    def __str__(self):
        return self.title

class Dropdown_for (models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    task = models.TextField(blank=True, verbose_name='Описание')
    datab = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    datas = models.DateTimeField(auto_now=True, verbose_name='Дата последного добавления')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фотография')
    is_pblished = models.BooleanField(default=True, verbose_name='Публирован')
    book = models.FileField(upload_to='static/%Y/%m/%d', blank=True, verbose_name='PDF книги')

    class Meta:
        verbose_name = 'Инновация категорий'
        verbose_name_plural = 'Инновация категорий'

    def __str__(self):
        return self.title

