# Generated by Django 3.2.16 on 2024-02-22 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20240130_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='post_images', verbose_name='Изображение'),
        ),
    ]