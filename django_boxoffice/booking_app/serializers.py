from django.forms import model_to_dict
from rest_framework import serializers
import models


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client


class RepresentativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Representatives


class ClientRepresentativeSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    representative = RepresentativeSerializer()
    class Meta:
        model = models.ClientRepresentatives
        fields = ('id',
                  'client',
                  'representative',
                  'representative_type',
                  'name',
                  'booking_price'
                  )


