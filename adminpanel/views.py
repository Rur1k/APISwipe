from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .serializers import (HouseCreateSerializer, HouseSerializer,
                          NotaryCreateSerializer, NotarySerializer,
                          FlatCreateSerializer, FlatSerializer,
                          UserSerializer)

from .models import House, Notary, Flat
from account.models import User


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


class FlatCreateAPIView(CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = FlatCreateSerializer


class FlatListAPIView(ListAPIView):
    queryset = Flat.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = FlatSerializer


class FlatAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Flat.objects.filter()
    permission_classes = (IsAdminUser,)
    serializer_class = FlatSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer


class BlacklistAPIView(ListAPIView):
    queryset = User.objects.filter(is_blacklist=True)
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer


class BlacklistSwitchAPIView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_blacklist:
            instance.is_blacklist = False
        else:
            instance.is_blacklist = True
        instance.save()

        return Response(status=status.HTTP_200_OK)

