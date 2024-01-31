import uuid

import geohash
from django.db import models
from django.conf import settings


class Business(models.Model):
    uid = models.UUIDField(
        primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    business_type = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)

    latitude = models.FloatField()
    longitude = models.FloatField()

    geohash = models.CharField(max_length=100)

    # Calculate the bounding box
    min_latitude = models.FloatField()
    max_latitude = models.FloatField()
    min_longitude = models.FloatField()
    max_longitude = models.FloatField()

    class Meta:
        unique_together = ['latitude', 'longitude']

    def save(self, *args, **kwargs):
        self.geohash = geohash.encode(
            self.latitude,
            self.longitude,
            precision=settings.GEOSEARCH_RANGE
        )
        # Get the bounding box for the geohash
        bbox = geohash.bbox(self.geohash)

        self.min_latitude = bbox['s']
        self.max_latitude = bbox['n']
        self.min_longitude = bbox['w']
        self.max_longitude = bbox['e']

        super().save(*args, **kwargs)
