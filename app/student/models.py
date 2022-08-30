from django.db import models
from app.mixins.db_classes import NameMixin
from app.user.models import User


class Student(NameMixin):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name="student"
    )

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.name
