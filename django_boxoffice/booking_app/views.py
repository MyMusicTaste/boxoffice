from django.shortcuts import render

# Create your views here.
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
def get_clients(request, id_numb=None):
    if id_numb:
        model_list = models.Client.objects.filter(pk=id_numb)
    else:
        model_list = models.Client.objects.all()

    if request.method == 'GET':
        serializer = serializers.ClientSerializer(model_list, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def get_client_representatives(request, id_numb=None):
    if id_numb:
        if request.method == 'GET':
            model_list = models.ClientRepresentatives.objects.values('representative_id').filter(client_id=id_numb)
            query = models.Representatives.objects.filter(pk__in=model_list)
            serializer = serializers.RepresentativeSerializer(query, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def get_representatives(request, id_numb=None):
    if id_numb:
        model_list = models.Representatives.objects.filter(pk=id_numb)
    else:
        model_list = models.Representatives.objects.all()

    if request.method == 'GET':
        serializer = serializers.RepresentativeSerializer(model_list, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def get_representatives_client(request, id_numb=None):
    if id_numb:
        if request.method == 'GET':
            model_list = models.ClientRepresentatives.objects.values('client_id').filter(representative_id=id_numb)
            query = models.Client.objects.filter(pk__in=model_list)
            serializer = serializers.ClientSerializer(query, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def get_clients_representatives(request, id_numb=None):
    if id_numb:
        model_list = models.ClientRepresentatives.objects.filter(pk=id_numb)
    else:
        model_list = models.ClientRepresentatives.objects.all()

    if request.method == 'GET':
        serializer = serializers.ClientRepresentativeSerializer(model_list, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)