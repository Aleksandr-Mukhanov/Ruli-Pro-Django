from django.contrib import admin
from .models import Subject, Question, Answer, Testing


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'ticket',
        'number_in_ticket',
        'subject'
    ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'is_answer',
        'question'
    ]


@admin.register(Testing)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'student',
        'question',
    ]
