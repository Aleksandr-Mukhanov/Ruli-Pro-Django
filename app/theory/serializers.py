from rest_framework import serializers
from .models import *


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'name', 'is_answer')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=False)

    class Meta:
        model = Question
        fields = ('id', 'name', 'ticket', 'number_in_ticket', 'note', 'answers', 'subject')
        depth = 2


class SubjectSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=False)

    class Meta:
        model = Subject
        fields = ('id', 'name', 'sort', 'category', 'questions')
        depth = 1
