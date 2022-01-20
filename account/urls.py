from django.urls import path, include
from .views import RegistrationAPIView, UserRetrieveUpdateAPIView

urlpatterns = [
    path('profile/', UserRetrieveUpdateAPIView.as_view()),
    path('user/reg', RegistrationAPIView.as_view()),
]
