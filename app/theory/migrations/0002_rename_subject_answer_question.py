# Generated by Django 4.0.5 on 2022-07-06 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='subject',
            new_name='question',
        ),
    ]