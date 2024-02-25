from django.db import models


class PublishedFlagModel(models.Model):
    """Абстрактная модель. Добвляет флаг is_published."""

    is_published = models.BooleanField(
        'Опубликовано',
        default=True,
        blank=False,
        help_text='Снимите галочку, чтобы скрыть публикацию.')

    class Meta:
        abstract = True


class CreatedFlagModel(models.Model):
    """Абстрактная модель. Добвляет флаг created_at."""

    created_at = models.DateTimeField(
        'Добавлено',
        auto_now_add=True,
        blank=False)

    class Meta:
        abstract = True
