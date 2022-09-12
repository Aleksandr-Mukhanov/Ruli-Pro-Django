from django.contrib import admin
from .models import Car


@admin.register(Car)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]
