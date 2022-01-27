from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # Модерация
    path('admin/house/', HouseViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('admin/house/<int:pk>', HouseViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'})),

    path('admin/flat/', FlatViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('admin/flat/<int:pk>', FlatViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'})),
    # Нотариусы
    path('admin/notary/', NotaryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('admin/notary/<int:pk>', NotaryViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'})),
    # Пользователи
    path('admin/users/', UserViewSet.as_view({'get': 'list'})),
    # Blacklist
    path('admin/blacklist/', BlacklistViewSet.as_view({'get': 'list'})),
    path('admin/blacklist/<int:pk>', BlacklistViewSet.as_view({'patch': 'update'})),

    # Для застройщика
    path('builder/house/', BuilderViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('builder/house/<int:pk>', BuilderViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'})),

    # Для пользователя
    path('announcement/', AnnouncementViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('announcement/<int:pk>', AnnouncementViewSet.as_view({'get': 'retrieve'})),

    path('announcement/my/', AnnouncementUserViewSet.as_view({'get': 'list'})),
    path('announcement/my/<int:pk>', AnnouncementUserViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'})),

]