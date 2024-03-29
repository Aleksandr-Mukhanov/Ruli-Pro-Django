# Generated by Django 4.0.5 on 2022-09-04 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '__first__'),
        ('theory', '0005_delete_mediafile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testing', to='theory.question', verbose_name='Вопрос')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testing', to='student.student', verbose_name='Ученик')),
            ],
        ),
    ]
