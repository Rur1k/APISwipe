from django.urls import path, include
from .views import UserViewSet, activation_email

urlpatterns = [
    path('profile/', UserViewSet.as_view({'get': 'retrieve', 'patch': 'update'})),
    path('activation/<ui>/<token>', activation_email)
]
