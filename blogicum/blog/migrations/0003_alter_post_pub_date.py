# Generated by Django 3.2.16 on 2024-01-28 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20240128_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(help_text='Если установить дату и время в будущем —можно делать отложенные публикации.', null=True, verbose_name='Дата и время публикации'),
        ),
    ]
