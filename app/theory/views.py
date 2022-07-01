from rest_framework import viewsets

from .models import *
from .serializers import *


class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
