from django.urls import path, include
from .views import UserViewSet

urlpatterns = [
    path('profile/', UserViewSet.as_view({'get': 'retrieve', 'patch': 'update'})),
]
