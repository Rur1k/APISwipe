from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # Модерация
    path('admin/house/create/', HouseCreateAPIView.as_view()),
    path('admin/house/list/', HouseListAPIView.as_view()),
    path('admin/house/<int:pk>', HouseAPIView.as_view()),

    path('admin/flat/create/', FlatCreateAPIView.as_view()),
    path('admin/flat/list/', FlatListAPIView.as_view()),
    path('admin/flat/<int:pk>', FlatAPIView.as_view()),
    # Нотариусы
    path('admin/notary/create/', NotaryCreateAPIView.as_view()),
    path('admin/notary/list/', NotaryListAPIView.as_view()),
    path('admin/notary/<int:pk>', NotaryAPIView.as_view()),
    # Пользователи
    path('admin/user/list/', UserListAPIView.as_view()),
    # Blacklist
    path('admin/blacklist/', BlacklistAPIView.as_view()),
    path('admin/blacklist/<int:pk>', BlacklistSwitchAPIView.as_view()),

    # Для застройщика
    path('builder/house/list/', BuilderHouseListAPIView.as_view()),
    path('builder/house/create/', BuilderHouseCreateAPIView.as_view()),
    path('builder/house/<int:pk>', BuilderHouseAPIView.as_view()),

    # Для пользователя
    path('announcement/create/', AnnouncementCreateAPIView.as_view()),
    path('announcement/list/', AnnouncementListAPIView.as_view()),
    path('announcement/my/list/', AnnouncementUserListAPIView.as_view()),
    path('announcement/my/<int:pk>', AnnouncementUserAPIView.as_view()),
    path('announcement/<int:pk>', AnnouncementDetailAPIView.as_view()),
    path('announcement/<int:pk>', AnnouncementDetailAPIView.as_view()),
    path('notary/list/', NotaryListAPIView.as_view()),
]