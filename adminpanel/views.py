from rest_framework import status
from rest_framework import generics
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .serializers import *

from .permissions import IsBuilder

from .models import House, Notary, Flat
from account.models import User

'''АДМИНСКИЕ ПРЕДСТАВЛЕНИЯ'''


class HouseCreateAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = HouseCreateSerializer


class HouseListAPIView(generics.ListAPIView):
    queryset = House.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = HouseSerializer


class HouseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.filter()
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = HouseSerializer
    http_method_names = ['get', 'patch', 'delete']


class NotaryCreateAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = NotaryCreateSerializer


class NotaryListAPIView(generics.ListAPIView):
    queryset = Notary.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = NotarySerializer


class NotaryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notary.objects.filter()
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = NotarySerializer
    http_method_names = ['get', 'patch', 'delete']


class FlatCreateAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = FlatCreateSerializer


class FlatListAPIView(generics.ListAPIView):
    queryset = Flat.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = FlatSerializer


class FlatAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flat.objects.filter()
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = FlatSerializer
    http_method_names = ['get', 'patch', 'delete']


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = UserSerializer


class BlacklistAPIView(generics.ListAPIView):
    queryset = User.objects.filter(is_blacklist=True)
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = UserSerializer


class BlacklistSwitchAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = UserSerializer
    http_method_names = ['patch']

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_blacklist:
            instance.is_blacklist = False
        else:
            instance.is_blacklist = True
        instance.save()

        return Response(status=status.HTTP_200_OK)


'''ПРЕДСТАВЛЕНИЯ СТРОИТЕЛЯ'''


class BuilderHouseListAPIView(APIView):
    permission_classes = (IsAuthenticated, IsBuilder,)
    serializer_class = HouseSerializer

    def get(self, request):
        houses_in_builder = House.objects.filter(builder=request.user)
        serializer = self.serializer_class(houses_in_builder, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BuilderHouseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.all()
    permission_classes = (IsAuthenticated, IsBuilder,)
    serializer_class = HouseSerializer
    http_method_names = ['get', 'patch', 'delete']

    def get_queryset(self):
        queryset = House.objects.none()
        user = self.request.user
        if user.role.id == 2:
            queryset = self.queryset.filter(builder=user)
        return queryset


class BuilderHouseCreateAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, IsBuilder,)
    serializer_class = HouseCreateSerializer



