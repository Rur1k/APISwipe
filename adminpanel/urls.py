from django.contrib import admin
from django.urls import path, include
from .views import (HouseCreateAPIView, HouseListAPIView, HouseAPIView,
                    NotaryCreateAPIView, NotaryListAPIView, NotaryAPIView,
                    FlatCreateAPIView, FlatListAPIView, FlatAPIView,
                    UserListAPIView, BlacklistAPIView, BlacklistSwitchAPIView)

urlpatterns = [
    # Модерация
    path('house/create/', HouseCreateAPIView.as_view()),
    path('house/list/', HouseListAPIView.as_view()),
    path('house/<int:pk>', HouseAPIView.as_view()),

    path('flat/create/', FlatCreateAPIView.as_view()),
    path('flat/list/', FlatListAPIView.as_view()),
    path('flat/<int:pk>', FlatAPIView.as_view()),

    # Нотариусы
    path('notary/create/', NotaryCreateAPIView.as_view()),
    path('notary/list/', NotaryListAPIView.as_view()),
    path('notary/<int:pk>', NotaryAPIView.as_view()),
    # Пользователи
    path('user/list/', UserListAPIView.as_view()),
    # Blacklist
    path('blacklist/', BlacklistAPIView.as_view()),
    path('blacklist/<int:pk>', BlacklistSwitchAPIView.as_view()),
]