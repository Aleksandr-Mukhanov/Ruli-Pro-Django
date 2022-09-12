from rest_framework import serializers
from app.theory.models import Answer, Question, Subject
from app.media.models import MediaFile


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ('id', 'url')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'name', 'is_answer')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=False)
    media = MediaSerializer(many=True, read_only=False)

    class Meta:
        model = Question
        fields = ('id', 'name', 'ticket', 'number_in_ticket', 'note', 'answers', 'subject', 'media')
        depth = 2


class SubjectSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=False)
    media = MediaSerializer(many=True, read_only=False)

    class Meta:
        model = Subject
        fields = ('id', 'name', 'sort', 'category', 'questions', 'media')
        depth = 1
