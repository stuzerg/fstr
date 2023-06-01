# Generated by Django 4.2.1 on 2023-06-01 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passag', '0018_alter_perevaladded_status_alter_uzers_cell'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perevaladded',
            name='status',
            field=models.CharField(choices=[(None, 'не указано'), ('new', 'новый'), ('pending', 'в работе'), ('accepted', 'принят'), ('rejected', 'отклонён')], default='new', verbose_name='статус модерации'),
        ),
    ]