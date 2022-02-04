from django.forms import model_to_dict
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from drf_psq import PsqMixin, Rule, psq

from .serializers import *
from .permissions import IsBuilder, IsCreatorFlat
from .models import House, Notary, Flat, Announcement, Favorite
from .service import AnnouncementFilter
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


'''ПРЕДСТАВЛЕНИЯ ПОЛЬЗОВАТЕЛЯ'''


class AnnouncementViewSet(PsqMixin, ModelViewSet):
    queryset = Announcement.objects.filter(pub_status=True)
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AnnouncementFilter

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
