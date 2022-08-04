from rest_framework import viewsets, generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CurrentUserView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return self.queryset.filter(auth_token=self.request.auth)
