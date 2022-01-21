from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import HouseSerializer
from .renderers import HouseJSONRenderer
from .models import House


class HouseAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = HouseSerializer
    renderer_classes = (HouseJSONRenderer, )

    def get(self, request):
        houses = House.objects.all()
        return Response(houses)

    def post(self, request):
        house = request.data.get('house', {})
        serializer = self.serializer_class(data=house)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)