import uuid

import geohash
from django.db import models

from  .utils import geosearch_precision


class Business(models.Model):
    uid = models.UUIDField(
        primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    business_type = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)

    latitude = models.FloatField()
    longitude = models.FloatField()

    geo_hash = models.CharField(max_length=100)

    class Meta:
        unique_together = ['latitude', 'longitude']

    def save(self, *args, **kwargs):
        self.geo_hash = geohash.encode(
            self.latitude,
            self.longitude,
            # Change GEOSEARCH_RANGE in settings.py to change it.
            precision=geosearch_precision()
        )

        super().save(*args, **kwargs)
