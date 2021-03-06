# Generated by Django 4.0.5 on 2022-07-06 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('sort', models.SmallIntegerField(default=500, verbose_name='Сортировка')),
                ('is_archive', models.BooleanField(default=False, verbose_name='Архив')),
                ('category', models.ManyToManyField(to='dictionary.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_archive', models.BooleanField(default=False, verbose_name='Архив')),
                ('note', models.CharField(max_length=200, verbose_name='Заметка')),
                ('ticket', models.SmallIntegerField(verbose_name='Номер')),
                ('number_in_ticket', models.SmallIntegerField(verbose_name='Номер в билете')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theory.subject', verbose_name='Тема')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_archive', models.BooleanField(default=False, verbose_name='Архив')),
                ('is_answer', models.BooleanField(default=False, verbose_name='Верный')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theory.question', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
