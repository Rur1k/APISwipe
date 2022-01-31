from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # Дома
    path('house/', HouseViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('house/<int:pk>', HouseViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'})),
    # Квартиры
    path('flat/', FlatViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('flat/<int:pk>', FlatViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'})),
    # Нотариусы
    path('notary/', NotaryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('notary/<int:pk>', NotaryViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'})),
    # Пользователи
    path('users/', UserViewSet.as_view({'get': 'list'})),
    path('users/blacklist/', BlacklistViewSet.as_view({'get': 'list'})),
    path('users/blacklist/<int:pk>', BlacklistViewSet.as_view({'patch': 'update'})),
    # Дома застройщика
    # path('builder/house/', BuilderViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('builder/house/<int:pk>', BuilderViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'})),
    # Объявления общие
    path('announcement/', AnnouncementViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('announcement/<int:pk>', AnnouncementViewSet.as_view({'get': 'retrieve'})),
    # Объявления пользователя
    path('announcement/my/', AnnouncementUserViewSet.as_view({'get': 'list'})),
    path('announcement/my/<int:pk>', AnnouncementUserViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'})),
    # Модерация
    path('announcement/moderation/', AnnouncementAdminViewSet.as_view({'get': 'list'})),
    path('announcement/moderation/<int:pk>',
         AnnouncementAdminViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'})),
    # Фильтры
    path('filter/', FilterAnnouncementViewSet.as_view({'get': 'list'})),
    path('filter/my/', UserFilterViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('filter/my/<int:pk>', UserFilterViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'})),


]