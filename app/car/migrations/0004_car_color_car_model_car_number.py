# Generated by Django 4.0.5 on 2022-09-16 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0002_carcolors_carmodels'),
        ('car', '0003_car_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='dictionary.carcolors', verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='dictionary.carmodels', verbose_name='Модель'),
        ),
        migrations.AddField(
            model_name='car',
            name='number',
            field=models.CharField(default=True, max_length=9, verbose_name='Номер'),
        ),
    ]