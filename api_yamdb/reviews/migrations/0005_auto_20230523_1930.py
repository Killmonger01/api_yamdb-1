# Generated by Django 3.2 on 2023-05-23 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_genres_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Слаг категории'),
        ),
        migrations.AlterField(
            model_name='genres',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название жанра'),
        ),
        migrations.AlterField(
            model_name='genres',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Слаг жанра'),
        ),
    ]