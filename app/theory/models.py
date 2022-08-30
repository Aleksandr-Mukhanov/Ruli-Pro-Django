from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from app.mixins.db_classes import NameMixin, CreatedUpdatedMixin, SortMixin, NoteMixin, IsArchiveMixin
from app.dictionary.models import Category
from app.media.models import MediaFile
from app.student.models import Student


class Subject(NameMixin, CreatedUpdatedMixin, SortMixin, IsArchiveMixin):
    media = GenericRelation(MediaFile)
    category = models.ManyToManyField(Category, verbose_name='Категория')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.name


class Question(NameMixin, CreatedUpdatedMixin, NoteMixin, IsArchiveMixin):
    media = GenericRelation(MediaFile)
    ticket = models.SmallIntegerField(verbose_name='Номер')
    number_in_ticket = models.SmallIntegerField(verbose_name='Номер в билете')
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        verbose_name='Тема',
        related_name="questions"
    )

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


class Testing(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name='Ученик',
        related_name="testing"
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name='Вопрос',
        related_name="testing"
    )
