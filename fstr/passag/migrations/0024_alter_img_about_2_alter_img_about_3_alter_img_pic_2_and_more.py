# Generated by Django 4.2.1 on 2023-06-06 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passag', '0023_alter_coords_height_alter_coords_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='about_2',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='описание фото_2'),
        ),
        migrations.AlterField(
            model_name='img',
            name='about_3',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='описание фото_3'),
        ),
        migrations.AlterField(
            model_name='img',
            name='pic_2',
            field=models.URLField(blank=True, default='', verbose_name='ссылка на фото_2'),
        ),
        migrations.AlterField(
            model_name='img',
            name='pic_3',
            field=models.URLField(blank=True, default='', verbose_name='ссылка на фото_3'),
        ),
    ]
