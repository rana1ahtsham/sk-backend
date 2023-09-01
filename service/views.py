from loguru import logger
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from service.models import Provider, Location, Nature
from service.serializers import ProviderSerializer, LocationSerializer, NatureSerializer


class ProviderView(APIView):
    def get(self, request):
        data = Provider.objects.all()
        serializer = ProviderSerializer(data, many=True)
        logger.info(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LocationView(APIView):
    def get(self, request):
        data = Location.objects.all()
        response = [
            location.name
            for location in data
        ]
        return Response(response, status=status.HTTP_200_OK)


class NatureView(APIView):
    def get(self, request):
        response = {}
        for nature in Nature.objects.all():
            response.setdefault(nature.type.title(), []).append(nature.name.title())

        return Response(response, status=status.HTTP_200_OK)
