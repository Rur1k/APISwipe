from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer
from .models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer

    # def get_queryset(self):
    #     queryset = User.objects.none()
    #     user = self.request.user
    #     if user:
    #         queryset = self.queryset.filter(pk=user.id)
    #     return queryset

    def retrieve(self, request, *args, **kwargs):
        queryset = self.queryset.filter(pk=request.user.id).first()
        serializer = self.serializer_class(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.queryset.filter(pk=request.user.id).first()
        instance.phone = request.data.get('phone')
        instance.first_name = request.data.get('first_name')
        instance.last_name = request.data.get('last_name')
        instance.save()
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)





