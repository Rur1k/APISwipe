from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import HouseCreateSerializer, HouseListSerializer
from .renderers import HouseJSONRenderer
from .models import House


class HouseListAPIView(APIView):
    def get(self, request):
        houses = House.objects.all()
        serializer = HouseListSerializer(houses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class HouseCreateAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = HouseCreateSerializer

    def post(self, request):
        house = request.data.get('house', {})
        serializer = self.serializer_class(data=house)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)