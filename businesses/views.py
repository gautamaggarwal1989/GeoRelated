from django.shortcuts import render
from rest_framework import generics

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
