from django.contrib import admin
from .models import Student


@admin.register(Student)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'user'
    ]
