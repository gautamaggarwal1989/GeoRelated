from decimal import Decimal

from rest_framework import serializers
import haversine

from .models import Business


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'

        extra_kwargs = {
            'geo_hash': {'required': False},
        }


class BusinessListSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField()

    def get_distance(self, obj):
        request = self.context.get('request')
        if request:
            lat = request.query_params.get('lat')
            lon = request.query_params.get('lon')

            lat, lon = Decimal(lat), Decimal(lon)

        return haversine.haversine((lat, lon), (obj.latitude, obj.longitude))

    class Meta:
        model = Business
        fields = '__all__'
