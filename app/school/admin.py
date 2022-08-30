from django.contrib import admin
from .models import *


@admin.register(School)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]


@admin.register(Member)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'school',
        'user'
    ]


@admin.register(TeacherInSchool)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'school',
    ]
