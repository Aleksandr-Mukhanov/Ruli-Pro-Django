from django.db import models
from app.mixins.db_classes import NameMixin
from app.user.models import User


class Teacher(NameMixin):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name="teacher"
    )

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.name
