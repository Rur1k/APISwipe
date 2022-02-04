from django.forms import model_to_dict
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from drf_psq import PsqMixin, Rule, psq

from .serializers import *
from .permissions import IsBuilder, IsCreatorFlat
from .models import House, Notary, Flat, Announcement, UserFilter, Favorite
from account.models import User

'''АДМИНСКИЕ ПРЕДСТАВЛЕНИЯ'''


class HouseViewSet(PsqMixin, ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [IsAdminUser]

    psq_rules = {
        ('list', 'retrieve'): [
            Rule([IsAuthenticated], serializer_class),
        ]
    }


class NotaryViewSet(PsqMixin, ModelViewSet):
    queryset = Notary.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = NotarySerializer

    psq_rules = {
        ('list', 'retrieve'): [
            Rule([IsAuthenticated], serializer_class),
        ]
    }


class FlatViewSet(PsqMixin, ModelViewSet):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    psq_rules = {
        'create': [Rule([IsAdminUser]), Rule([IsBuilder])],
        ('update', 'destroy'): [
            Rule([IsAdminUser]),
            Rule([IsCreatorFlat], get_obj=lambda self, obj:self.get_object()),
        ],
        ('list', 'retrieve'): [
            Rule([IsBuilder], serializer_class, lambda self:self.queryset.filter(creator=self.request.user)),
            Rule([IsAuthenticated]),
        ],
    }


class FlatReservedViewSet(PsqMixin, ModelViewSet):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer

    psq_rules = {
        'update': [
            Rule([IsAdminUser]),
            Rule([IsCreatorFlat], get_obj=lambda self, obj: self.get_object()),
        ],
    }

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.reserved:
            instance.reserved = False
        else:
            instance.reserved = True
        instance.save()
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserViewSet(PsqMixin, ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer


class BlacklistViewSet(PsqMixin, ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
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


# class BuilderViewSet(PsqMixin, ModelViewSet):
#     queryset = House.objects.all()
#     serializer_class = HouseSerializer
#
#     psq_rules = {
#         ('list', 'create', 'retrieve', 'update', 'destroy'): [
#             Rule([IsAdminUser], serializer_class),
#             Rule([IsBuilder], serializer_class),
#         ]
#     }
#
#     def get_queryset(self):
#         queryset = House.objects.none()
#         user = self.request.user
#         if user:
#             queryset = self.queryset.filter(builder=user)
#         return queryset
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


'''ПРЕДСТАВЛЕНИЯ ПОЛЬЗОВАТЕЛЯ'''


class AnnouncementViewSet(PsqMixin, ModelViewSet):
    queryset = Announcement.objects.filter(pub_status=True)
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AnnouncementUserViewSet(PsqMixin, ModelViewSet):
    queryset = Announcement.objects.all()
    permission_classes = [IsAuthenticated]
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


class AnnouncementAdminViewSet(PsqMixin, ModelViewSet):
    queryset = Announcement.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = AnnouncementSerializer


class FilterAnnouncementViewSet(PsqMixin, ModelViewSet):
    queryset = Announcement.objects.filter(pub_status=True)
    permission_classes = [IsAuthenticated]
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


class UserFilterViewSet(PsqMixin, ModelViewSet):
    queryset = UserFilter.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserFilterSerializer

    def get_queryset(self):
        queryset = UserFilter.objects.none()
        user = self.request.user
        if user:
            queryset = self.queryset.filter(user=user)
        return queryset


class FavoriteViewSet(PsqMixin, ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Favorite.objects.none()
        user = self.request.user
        if user:
            queryset = self.queryset.filter(user=user)
            print(queryset)
        return queryset


class GalleryViewSet(ModelViewSet):
    queryset = GalleryAnnouncement.objects.all()
    serializer_class = GalleryAnnouncementSerializer
    permission_classes = [IsAuthenticated]
