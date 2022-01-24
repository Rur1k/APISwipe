from django.urls import path, include
from .views import UserRetrieveUpdateAPIView

urlpatterns = [
    path('profile/', UserRetrieveUpdateAPIView.as_view()),
]
