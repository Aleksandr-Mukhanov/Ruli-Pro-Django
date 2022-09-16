from django.db import models
from app.mixins.db_classes import NameMixin
from app.dictionary.models import Category, CarModels, CarColors
from app.teacher.models import Teacher


class Car(NameMixin):
    owner = models.ManyToManyField(Teacher, verbose_name='Владелец')
    number = models.CharField(max_length=9, verbose_name='Номер')
    model = models.ForeignKey(CarModels, on_delete=models.CASCADE, verbose_name='Модель')
    color = models.ForeignKey(CarColors, on_delete=models.CASCADE, verbose_name='Цвет')
    year = models.IntegerField(verbose_name='Год')

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return self.name
