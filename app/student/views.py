from rest_framework import viewsets
from .models import *
from .serializers import *


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
