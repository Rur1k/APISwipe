from django.contrib import admin
from django.urls import path, include
from .views import (HouseCreateAPIView, HouseListAPIView, HouseAPIView,
                    NotaryCreateAPIView, NotaryListAPIView, NotaryAPIView,
                    FlatCreateSerializer, FlatListAPIView, FlatAPIView)

urlpatterns = [
    # Модерация
    path('house/create/', HouseCreateAPIView.as_view()),
    path('house/list/', HouseListAPIView.as_view()),
    path('house/<int:pk>', HouseAPIView.as_view()),

    path('flat/create/', HouseCreateAPIView.as_view()),
    path('flat/list/', HouseListAPIView.as_view()),
    path('flat/<int:pk>', HouseAPIView.as_view()),

    # Нотариусы
    path('notary/create/', NotaryCreateAPIView.as_view()),
    path('notary/list/', NotaryListAPIView.as_view()),
    path('notary/<int:pk>', NotaryAPIView.as_view()),
]