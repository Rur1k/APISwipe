from django.contrib import admin
from django.urls import path, include
from .views import HouseAPIView

urlpatterns = [
    path('house/', HouseAPIView.as_view()),
]