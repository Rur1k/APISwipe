from django.forms import model_to_dict
from rest_framework import status
from rest_framework import generics
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import *

from .permissions import IsBuilder

from .models import House, Notary, Flat, Announcement, UserFilter
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


class FilterAnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.filter(pub_status=True)
    permission_classes = (IsAuthenticated,)
    serializer_class = AnnouncementSerializer

    def get_queryset(self):
        queryset = self.queryset
        data = self.request.data
        if 'id' in data:
            obj = UserFilter.objects.filter(id=data.get('id')).first()
            if obj:
                data = model_to_dict(obj)
                if data['user'] == self.request.user.id:
                    if data['state_house']:
                        queryset = queryset.filter(house__state=data['state_house'])
                    if data['district']:
                        queryset = queryset.filter(house__district=data['district'])
                    if data['microdistrict']:
                        queryset = queryset.filter(house__microdistrict=data['microdistrdata'])
                    if data['count_rooms']:
                        queryset = queryset.filter(count_rooms=data['count_rooms'])
                    if data['price_first']:
                        queryset = queryset.filter(price__gte=data['price_first'])
                    if data['price_last']:
                        queryset = queryset.filter(price__lte=data['price_last'])
                    if data['square_first']:
                        queryset = queryset.filter(all_square__gte=data['square_first'])
                    if data['square_last']:
                        queryset = queryset.filter(all_square__lte=data['square_last'])
                    if data['purpose']:
                        queryset = queryset.filter(purpose=data['purpose'])
                    if data['calculation_option']:
                        queryset = queryset.filter(calculation_option=data['calculation_option'])
                    if data['residential_condition']:
                        queryset = queryset.filter(residential_condition=data['residential_condition'])
        else:
            if 'state_house' in data:
                queryset = queryset.filter(house__state=data.get('state_house'))
            if 'district' in data:
                queryset = queryset.filter(house__district=data.get('district'))
            if 'microdistrict' in data:
                queryset = queryset.filter(house__microdistrict=data.get('microdistrict'))
            if 'count_rooms' in data:
                queryset = queryset.filter(count_rooms=data.get('count_rooms'))
            if 'price_first' in data:
                queryset = queryset.filter(price__gte=data.get('price_first'))
            if 'price_last' in data:
                queryset = queryset.filter(price__lte=data.get('price_last'))
            if 'square_first' in data:
                queryset = queryset.filter(all_square=data.get('square_first'))
            if 'square_last' in data:
                queryset = queryset.filter(all_square=data.get('square_last'))
            if 'purpose' in data:
                queryset = queryset.filter(purpose=data.get('purpose'))
            if 'calculation_option' in data:
                queryset = queryset.filter(calculation_option=data.get('calculation_option'))
            if 'residential_condition' in data:
                queryset = queryset.filter(residential_condition=data.get('residential_condition'))

        return queryset


class UserFilterViewSet(ModelViewSet):
    queryset = UserFilter.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserFilterSerializer

    def get_queryset(self):
        queryset = UserFilter.objects.none()
        user = self.request.user
        if user:
            queryset = self.queryset.filter(user=user)
        return queryset
