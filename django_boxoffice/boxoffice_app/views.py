# -*- coding: utf-8 -*-
import datetime

from dateutil import parser
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import models
import serializers


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
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
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
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
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
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
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
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
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
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
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
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
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def get_events(request, id_numb=None):
    if request.query_params:
        default_date = datetime.datetime(datetime.MINYEAR, 1, 1)
        paramQueryDict = dict(request.query_params.iterlists())

        if paramQueryDict.has_key('start_date'):
            sdt = parser.parse(request.query_params['start_date'], default=default_date, fuzzy=True)
            start_date = sdt.date()

            if paramQueryDict.has_key('end_date') and request.query_params['end_date']:
                ldt = parser.parse(request.query_params['end_date'], default=default_date, fuzzy=True)
                end_date = ldt.date()
                date_query = models.Date.objects.values('event_id').filter(event_date__range=[start_date, end_date]).distinct()
            else:
                date_query = models.Date.objects.values('event_id').filter(event_date__gte=start_date).distinct()

            date_list = models.Event.objects.filter(pk__in=date_query).order_by('-sale')

            serializer = serializers.EventSerializer(date_list, many=True)
            return Response(serializer.data)
        elif paramQueryDict.has_key('start_index'):
            start_index = int(request.query_params['start_index'])
            end_index = int(request.query_params['end_index'])

            model_all = models.Event.objects.all().order_by('-sale')[start_index:end_index]
            serializer = serializers.EventSerializer(model_all, many=True)
            return Response(serializer.data)
        else:
            date_query = models.Date.objects.values('event_id').filter(event_date__gte=default_date.date()).distinct()
            date_list = models.Event.objects.filter(pk__in=date_query).order_by('-sale')
            serializer = serializers.EventSerializer(date_list, many=True)
            return Response(serializer.data)
    else:
        if id_numb:
            model_all = models.Event.objects.filter(pk=id_numb)
        else:
            model_all = models.Event.objects.all().order_by('-sale')

        if request.method == 'GET':
            serializer = serializers.EventSerializer(model_all, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            return Response(status=status.HTTP_400_BAD_REQUEST)
