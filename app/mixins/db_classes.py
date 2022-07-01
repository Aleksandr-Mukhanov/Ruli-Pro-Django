from django.db import models


class IsActiveMixin(models.Model):
    is_active = models.BooleanField(verbose_name='Активность', default=True)

    class Meta:
        abstract = True


class NameMixin(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    class Meta:
        abstract = True


class CreatedUpdatedMixin(models.Model):
    date_create = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    date_update = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)

    class Meta:
        abstract = True


class SortMixin(models.Model):
    sort = models.SmallIntegerField(verbose_name='Сортировка', default=500)

    class Meta:
        abstract = True


class IsArchiveMixin(models.Model):
    is_archive = models.BooleanField(verbose_name='Архив', default=False)

    class Meta:
        abstract = True


class NoteMixin(models.Model):
    note = models.CharField(max_length=200, verbose_name='Заметка')

    class Meta:
        abstract = True
