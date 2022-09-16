from django.contrib import admin
from .models import Schedule


@admin.register(Schedule)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'datetime',
        'student',
        'teacher',
        'car',
        'date_create',
        'date_update'
    ]
