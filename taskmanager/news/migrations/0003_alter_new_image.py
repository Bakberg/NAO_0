# Generated by Django 3.2.6 on 2021-09-01 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_new_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фотография'),
        ),
    ]
