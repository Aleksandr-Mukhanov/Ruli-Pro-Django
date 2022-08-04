from django.db import models
from app.mixins.db_classes import NameMixin, CreatedUpdatedMixin, SortMixin, NoteMixin, IsArchiveMixin
from app.dictionary.models import Category


class Subject(NameMixin, CreatedUpdatedMixin, SortMixin, IsArchiveMixin):
    category = models.ManyToManyField(Category, verbose_name='Категория')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.name


class Question(NameMixin, CreatedUpdatedMixin, NoteMixin, IsArchiveMixin):
    ticket = models.SmallIntegerField(verbose_name='Номер')
    number_in_ticket = models.SmallIntegerField(verbose_name='Номер в билете')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Тема')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.name


class Answer(NameMixin, CreatedUpdatedMixin, IsArchiveMixin):
    is_answer = models.BooleanField(verbose_name='Верный', default=False)
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name='Вопрос',
        related_name="answers"
    )

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.name
