from rest_framework import status
from rest_framework import generics
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import *

from .permissions import IsBuilder

from .models import House, Notary, Flat, Announcement
from account.models import User

'''АДМИНСКИЕ ПРЕДСТАВЛЕНИЯ'''


class HouseViewSet(ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = (IsAuthenticated, IsAdminUser,)


class NotaryViewSet(ModelViewSet):
    queryset = Notary.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = NotarySerializer


class FlatViewSet(ModelViewSet):
    queryset = Flat.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = FlatSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = UserSerializer


class BlacklistViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser,)
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        queryset = User.objects.filter(is_blacklist=True)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_blacklist:
            instance.is_blacklist = False
        else:
            instance.is_blacklist = True
        instance.save()
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


'''ПРЕДСТАВЛЕНИЯ СТРОИТЕЛЯ'''


class BuilderViewSet(ModelViewSet):
    queryset = House.objects.all()
    permission_classes = (IsAuthenticated, IsBuilder,)
    serializer_class = HouseSerializer

    def get_queryset(self):
        queryset = House.objects.none()
        user = self.request.user
        if user.role.id == 2:
            queryset = self.queryset.filter(builder=user)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)




'''ПРЕДСТАВЛЕНИЯ ПОЛЬЗОВАТЕЛЯ'''


class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.filter(pub_status=True)
    permission_classes = (IsAuthenticated,)
    serializer_class = AnnouncementSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AnnouncementUserViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = AnnouncementSerializer

    def get_queryset(self):
        queryset = Announcement.objects.none()
        user = self.request.user
        if user:
            queryset = self.queryset.filter(user=user)
        return queryset

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.pub_status = False
        instance.save()
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
