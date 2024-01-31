from rest_framework import filters


class ProximityFilter(filters.BaseFilterBackend):
    ''' Filtering on the basis of location from where
    the request was made so as to provide client with shops
    data that are in proximity of 5 kilometers as geohashing
    is using a precision of 6 for our example.'''

    def filter_queryset(self, request, queryset, view):
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')

        if lat is None or lon is None:
            raise Exception("Lattitude and longitude are mandatory!")
        
        # Get the geohashes in whose binding box
        # latitude and longitude falls into.
        queryset = queryset.filter(
           min_latitude__lt=lat,
           max_latitude__gt=lat,
           min_longitude__lt=lon,
           max_longitude__gt=lon
        )

        return queryset
