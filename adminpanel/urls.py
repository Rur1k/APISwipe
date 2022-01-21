from django.contrib import admin
from django.urls import path, include
from .views import HouseCreateAPIView, HouseListAPIView

urlpatterns = [
    path('house/', HouseCreateAPIView.as_view()),
    path('houses/', HouseListAPIView.as_view()),
]