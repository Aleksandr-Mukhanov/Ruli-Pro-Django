from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'user'
    ]
