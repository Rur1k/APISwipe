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
    path('flat/reserved/<int:pk>', FlatReservedViewSet.as_view({'patch': 'update'})),
    # Нотариусы
    path('notary/', NotaryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('notary/<int:pk>', NotaryViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'})),
    # Пользователи
    path('users/', UserViewSet.as_view({'get': 'list'})),
    path('users/blacklist/', BlacklistViewSet.as_view({'get': 'list'})),
    path('users/blacklist/<int:pk>', BlacklistViewSet.as_view({'patch': 'update'})),
    # Объявления общие
    path('announcement/', AnnouncementViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('announcement/<int:pk>', AnnouncementViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'})),
    # Объявления пользователя
    path('announcement/my/', AnnouncementUserViewSet.as_view({'get': 'list'})),
    path('announcement/my/<int:pk>', AnnouncementUserViewSet.as_view({'get': 'retrieve'})),
    # Галерея
    path('announcement/img/', GalleryViewSet.as_view({'post': 'create'})),
    # Избранное
    path('favorite/', FavoriteViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('favorite/<int:pk>', FavoriteViewSet.as_view({'delete': 'destroy'})),

]
