from rest_framework import serializers
from service.models import Provider, Location, Nature


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']


class NatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nature
        fields = ['id', 'name', 'type']


class ProviderSerializer(serializers.ModelSerializer):
    service_location = LocationSerializer()
    service_nature = NatureSerializer()

    class Meta:
        model = Provider
        fields = '__all__'
