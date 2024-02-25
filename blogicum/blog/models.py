from django.contrib.auth import get_user_model
from django.db import models

from core.constants import (CATEGORY_TITLE_MAX_LEN,
                            COMMENT_TEXT_MAX_LEN,
                            LOCATION_NAME_MAX_LEN,
                            POST_TITLE_MAX_LEN)
from core.models import PublishedFlagModel, CreatedFlagModel

User = get_user_model()  # Пользователь


class Location(PublishedFlagModel, CreatedFlagModel):
    name = models.CharField('Название места', max_length=LOCATION_NAME_MAX_LEN)

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Category(PublishedFlagModel, CreatedFlagModel):
    title = models.CharField('Заголовок', max_length=CATEGORY_TITLE_MAX_LEN)
    description = models.TextField('Описание')
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        help_text='Идентификатор страницы для URL; разрешены символы '
                  'латиницы, цифры, дефис и подчёркивание.')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Post(PublishedFlagModel, CreatedFlagModel):
    title = models.CharField('Заголовок', max_length=POST_TITLE_MAX_LEN)
    text = models.TextField('Текст')
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        null=True,
        blank=False,
        help_text='Если установить дату и время в будущем — можно делать '
                  'отложенные публикации.')
    image = models.ImageField('Изображение',
                              upload_to='post_images', blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор публикации')
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name='Местоположение')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts',
        verbose_name='Категория')

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title


class Comment(PublishedFlagModel, CreatedFlagModel):
    text = models.TextField('Текст комментария',
                            max_length=COMMENT_TEXT_MAX_LEN)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор комментария',
        related_name='comments'
    )

    class Meta:
        verbose_name = 'коментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ('created_at',)

    def __str__(self):
        return self.text
