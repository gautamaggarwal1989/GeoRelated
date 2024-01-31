from decimal import Decimal
import haversine

import geohash
from rest_framework import filters

from  .utils import geosearch_precision


class ProximityFilter(filters.BaseFilterBackend):
    ''' Filtering on the basis of location from where
    the request was made so as to provide client with shops
    data that are in proximity of 5 kilometers as geohashing
    is using a precision of 5 for our example.'''

    def filter_queryset(self, request, queryset, view):
        lat = Decimal(request.GET.get('lat'))
        lon = Decimal(request.GET.get('lon'))

        if lat is None or lon is None:
            raise Exception("Lattitude and longitude are mandatory!")
        
        geo_hash = geohash.encode(
            lat, lon, precision=geosearch_precision())
        
        # Get neighbouring geohashes
        geohashes = geohash.neighbors(geo_hash)
        geohashes.append(geo_hash)

        queryset = queryset.filter(
           geo_hash__in=geohashes
        )

        return queryset
