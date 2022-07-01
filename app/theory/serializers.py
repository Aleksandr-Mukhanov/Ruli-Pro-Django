from rest_framework import serializers
from .models import *


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'name', 'ticket', 'number_in_ticket', 'subject', 'note')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'name', 'is_answer', 'question')
