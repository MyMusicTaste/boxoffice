# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import models
import json
import datetime
from dateutil import parser
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# @csrf_exempt


@api_view(['GET'])
def get_artists(request, id_numb=None):
    if id_numb:
        model_all = models.ArtistEvent.objects.filter(pk=id_numb)
    else:
        model_all = models.ArtistEvent.objects.all()

    if request.method == 'GET':
        serializer = serializers.ArtistEventSerializer(model_all, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_artist_event(request, id_numb=None):
    if id_numb:
        model_list = models.Event.objects.filter(artist_event_id=id_numb)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = serializers.EventSerializer(model_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_promoters(request, id_numb=None):
    if id_numb:
        model_all = models.Promoter.objects.filter(pk=id_numb)
    else:
        model_all = models.Promoter.objects.all()

    if request.method == 'GET':
        serializer = serializers.PromoterSerializer(model_all, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_promoter_event(request, id_numb=None):
    if id_numb:
        model_list = models.Event.objects.filter(promoters__promoter_id=id_numb)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = serializers.EventSerializer(model_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_cities(request, id_numb=None):
    if id_numb:
        model_all = models.City.objects.filter(pk=id_numb)
    else:
        model_all = models.City.objects.all()

    if request.method == 'GET':
        serializer = serializers.CitySerializer(model_all, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_city_event(request, id_numb=None):
    if id_numb:
        model_list = models.Event.objects.filter(city_id=id_numb)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = serializers.EventSerializer(model_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_events(request, id_numb=None):
    if id_numb:
        model_all = models.Event.objects.filter(pk=id_numb)
    else:
        model_all = models.Event.objects.all()

    if request.method == 'GET':
        serializer = serializers.EventSerializer(model_all, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_event_dates(request, s_date=None, e_date=None):
    if s_date:
        default_date = datetime.datetime(datetime.MINYEAR, 1, 1)
        sdt = parser.parse(s_date, default=default_date, fuzzy=True)
        start_date = sdt.date()

        if e_date:
            ldt = parser.parse(e_date, default=default_date, fuzzy=True)
            end_date = ldt.date()
            date_query = models.Date.objects.values('event_id').filter(event_date__range=[start_date, end_date]).distinct()
        else:
            date_query = models.Date.objects.values('event_id').filter(event_date__gte=start_date).distinct()

        date_list = models.Date.objects.filter(event__in=date_query)

        serializer = serializers.DateSerializer(date_list, many=True)
        return Response(serializer.data)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

