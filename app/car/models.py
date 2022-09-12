from django.db import models
from app.mixins.db_classes import NameMixin
from app.teacher.models import Teacher


class Car(NameMixin):
    owner = models.ManyToManyField(Teacher)

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return self.name
