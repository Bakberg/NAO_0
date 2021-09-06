from django.db import models

class New (models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    task = models.TextField(blank=True, verbose_name='Описание')
    datab = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    datas = models.DateTimeField(auto_now=True, verbose_name='Дата последного добавления')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фотография')
    is_pblished = models.BooleanField(default=True, verbose_name='Публирован')

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

class Last_new (models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    task = models.TextField(blank=True, verbose_name='Описание')
    datab = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    datas = models.DateTimeField(auto_now=True, verbose_name='Дата последного добавления')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фотография')
    is_pblished = models.BooleanField(default=True, verbose_name='Публирован')

    class Meta:
        verbose_name = 'Последние новости'
        verbose_name_plural = 'Последние новости'

    def __str__(self):
        return self.title



