# Generated by Django 5.0.1 on 2024-01-30 16:45

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('business_type', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('geohash', models.CharField(max_length=100)),
                ('min_latitude', models.FloatField()),
                ('max_latitude', models.FloatField()),
                ('min_longitude', models.FloatField()),
                ('max_longitude', models.FloatField()),
            ],
        ),
    ]
