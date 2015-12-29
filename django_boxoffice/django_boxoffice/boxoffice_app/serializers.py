# from django.contrib.auth.models import User, Group
from rest_framework import serializers
import models


class UpdateLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UpdateLog
        fields = ('id', 'last_update')


class ArtistEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArtistEvent
        fields = ('id', 'name')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = ('id', 'name', 'state')


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Venue
        fields = ('id', 'name')


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Price
        fields = ('id', 'price')


class PromoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Promoter
        fields = ('id', 'name')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = ('id',
                  'artist_event',
                  'city',
                  'venue',
                  'sale',
                  'attend',
                  'capacity',
                  'show',
                  'sellout',
                  'rank',
                  'dates',
                  'create_date')


class EventPromoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EventPromoter
        fields = ('id', 'event', 'promoter')


class EventPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EventPrice
        fields = ('id', 'event', 'price')


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Date
        fields = ('id', 'event', 'event_date')


class ErrorLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ErrorLog
        fields = ('id',
                  'table_name',
                  'artist_event',
                  'city',
                  'venue',
                  'attend_capacity',
                  'gross_sales',
                  'show_sellout',
                  'rank',
                  'dates',
                  'prices',
                  'promoters',
                  'create_date')

