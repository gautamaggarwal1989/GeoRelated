from django.shortcuts import render
from rest_framework import generics
from django.conf import settings

from .models import Business
from .serializers import BusinessSerializer, BusinessListSerializer
from .filters import ProximityFilter


class BusinessAPIView(generics.CreateAPIView):
    ''' Creating List and Create seperately.'''
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer


class NearByView(generics.ListAPIView):
    ''' Api logic to find the closest businesses to given point.
    '''
    queryset = Business.objects.all()
    serializer_class = BusinessListSerializer
    filter_backends = [ProximityFilter]

    def get_serializer_context(self):
        context = super(NearByView, self).get_serializer_context()
        context['request'] = self.request

        return context
    
    def list(self, *args, **kwargs):
        ''' Filtering the output on the basis of maximum distance.
        Note: We cannot do this in queryset or serializer as we do filtering
        on the basis of calculated field that is distance.'''
        response = super().list(*args, **kwargs)

        results = response.data['results']
        modified_results = []
        for result in results:
            if result['distance'] <= settings.GEOSEARCH_RANGE:
                modified_results.append(result)

        response.data['results'] = modified_results
        return response
