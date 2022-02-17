from urllib import request
from rest_framework import generics, viewsets
from rest_framework import permissions

from .models import UserNet
from .serializers import GetUserNetSerializer, GetUserNetPublicSerializer


class UserNetPublicView(viewsets.ModelViewSet):
    """Получение публичных данных пользователя"""

    queryset = UserNet.objects.all()
    serializer_class = GetUserNetPublicSerializer
    permission_classes = [permissions.AllowAny]


class UserNetView(viewsets.ModelViewSet):
    """Получение личных данных пользователя"""

    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)
