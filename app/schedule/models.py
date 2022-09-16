from django.db import models
from app.mixins.db_classes import CreatedUpdatedMixin
from app.student.models import Student
from app.teacher.models import Teacher
from app.car.models import Car


class Schedule (CreatedUpdatedMixin):
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Дата и время вождения')
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        verbose_name='Ученик',
        related_name="student")
    teacher = models.OneToOneField(
        Teacher,
        on_delete=models.CASCADE,
        verbose_name='Препод',
        related_name="teacher")
    car = models.OneToOneField(
        Car,
        on_delete=models.CASCADE,
        verbose_name='Авто',
        related_name="car")

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'

    # def __str__(self):
    #     return self.datetime
