# Generated by Django 3.2.16 on 2024-02-22 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]
