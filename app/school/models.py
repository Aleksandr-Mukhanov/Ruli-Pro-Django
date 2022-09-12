from django.db import models
from app.mixins.db_classes import NameMixin
from app.teacher.models import Teacher
from app.user.models import User


class School(NameMixin):
    teachers = models.ManyToManyField(Teacher)

    class Meta:
        verbose_name = 'Автошкола'
        verbose_name_plural = 'Автошколы'

    def __str__(self):
        return self.name


class Member(NameMixin):
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        verbose_name='Автошкола',
        related_name="member"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name="member"
    )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.name
