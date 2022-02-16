from rest_framework import generics

from .models import UserNet
from .serializers import GetUseNerSerializer


class GetUserNetView(generics.RetrieveAPIView):
    queryset = UserNet.objects.all()
    serializer_class = GetUseNerSerializer
