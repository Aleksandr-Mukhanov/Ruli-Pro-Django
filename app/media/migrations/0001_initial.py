# Generated by Django 4.0.5 on 2022-08-19 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200, verbose_name='URL')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.AddIndex(
            model_name='mediafile',
            index=models.Index(fields=['content_type', 'object_id'], name='media_media_content_43cba4_idx'),
        ),
    ]
