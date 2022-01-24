from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


from .serializers import (HouseCreateSerializer, HouseSerializer,
                          NotaryCreateSerializer, NotarySerializer,)
from .models import House, Notary


class HouseCreateAPIView(CreateAPIView):
    permission_classes = (IsAdminUser, )
    serializer_class = HouseCreateSerializer


class HouseListAPIView(ListAPIView):
    queryset = House.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = HouseSerializer


class HouseAPIView(RetrieveUpdateDestroyAPIView):
    queryset = House.objects.filter()
    permission_classes = (IsAdminUser,)
    serializer_class = HouseSerializer


class NotaryCreateAPIView(CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = NotaryCreateSerializer


class NotaryListAPIView(ListAPIView):
    queryset = Notary.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = NotarySerializer


class NotaryAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Notary.objects.filter()
    permission_classes = (IsAdminUser,)
    serializer_class = NotarySerializer

