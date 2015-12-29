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
def get_artists(request, artist_id=None):
    """
    코드 조각을 모두 보여주거나 새 코드 조각을 만듭니다.
    """
    if artist_id:
        model_all = models.ArtistEvent.objects.filter(pk=artist_id).values()
    else:
        model_all = models.ArtistEvent.objects.all()

    if request.method == 'GET':
        serializer = serializers.ArtistEventSerializer(model_all, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_artist_event(request, artist_id=None):
    if artist_id:
        model_list = models.Event.objects.filter(artist_event_id=1)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = serializers.EventSerializer(model_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        return Response(status=status.HTTP_400_BAD_REQUEST)


# return json : {"Date" : [{"event_id":"", "event_date":""}, ...]}
# def get_artist_event(request, artist_id=0):
#     return_dict = list()
#
#     if artist_id == 0:
#         array = models.ArtistEvent.objects.all()
#         for artist in array:
#             return_dict.append({"id": artist.id, "name": artist.name})
#     else:
#         artist = models.ArtistEvent.objects.get(pk=artist_id)
#         return_dict.append({"id": artist.id, "name": artist.name})
#
#     n = json.dumps(return_dict)
#     json_string = '{"ArtistEvent" : %s}' % n
#     return HttpResponse(json_string)
#
#
# # return json : {"ArtistEvent" : [{"id":"", "artist_event":""}, ...]}
# def get_promoter(request, promoter_id=0):
#     return_dict = list()
#
#     if promoter_id == 0:
#         array = models.Promoter.objects.all()
#         for promoter in array:
#             return_dict.append({"id": promoter.id, "name": promoter.name})
#     else :
#         promoter = models.Promoter.objects.get(pk=promoter_id)
#         return_dict.append({"id": promoter.id, "name": promoter.name})
#
#     n = json.dumps(return_dict)
#     json_string = '{"Promoter" : %s}' % n
#     return HttpResponse(json_string)
#
#
# # return json : {"Promoter" : [{"id":"", "promoter":""}, ...]}
# def get_event(request, parameter=None, param_id=None):
#     return_dict = list()
#
#     # update_log = models.UpdateLog.objects.get(pk=1)
#     # update_date = update_log.last_update
#
#     if parameter == None:
#         if param_id == None:
#             event_list = models.Event.objects.all().order_by('-sale')
#             for event in event_list:
#                 # if event.create_date == update_date:
#                 return_dict.append(get_event_dict(event))
#         else:
#             event = models.Event.objects.get(pk=param_id)
#             return_dict.append(get_event_dict(event))
#
#     else:
#         if parameter == "artist":
#             event_list = models.Event.objects.filter(artist_event_id=param_id).order_by('-sale')
#             return_dict = get_distinct_event_list(event_list)
#
#
#         elif parameter == 'venue':
#             event_list = models.Event.objects.filter(venue_id=param_id).order_by('-sale')
#             return_dict = get_distinct_event_list(event_list)
#
#         elif parameter == 'city':
#             event_list = models.Event.objects.filter(city_id=param_id).order_by('-sale')
#             return_dict = get_distinct_event_list(event_list)
#
#         elif parameter == 'promoter':
#             promoter_list = models.EventPromoter.objects.filter(promoter_id=param_id)
#             for event_promoter in promoter_list:
#                 event_list = models.Event.objects.filter(id=event_promoter.event_id).order_by('-sale')
#                 return_dict = get_distinct_event_list(event_list)
#
#     n = json.dumps(return_dict)
#     json_string = '{"Event" : %s}' % n
#     return HttpResponse(json_string)
#
#
# # return json :
# # {"Event" :
# # [{"city": {"state": "", "id":, "name": ""},
# #  "dates": "",
# # "capacity": ,
# # "attend": ,
# def get_date(request, sdate=None, ldate=None):
#     return_list = list()
#
#     # update_log = models.UpdateLog.objects.get(pk=1)
#     # update_date = update_log.last_update
#
#     if sdate is None:
#         date_list = models.Date.objects.values('event_id').all().distinct()
#
#         return_list = list()
#         for date in date_list:
#             event = models.Event.objects.get(pk=date['event_id'])
#             # if event.create_date == update_date:
#             return_list.append(get_event_dict(event))
#
#     else:
#         default_date = datetime.datetime(datetime.MINYEAR, 1, 1)
#         sdt = parser.parse(sdate, default=default_date, fuzzy=True)
#         first_date = sdt.date()
#
#         if ldate is None:
#             date_list = models.Date.objects.values('event_id').filter(event_date__gte=first_date).distinct()
#             for date in date_list:
#                 event = models.Event.objects.get(pk=date['event_id'])
#                 # if event.create_date == update_date:
#                 return_list.append(get_event_dict(event))
#
#         else:
#             ldt = parser.parse(ldate, default=default_date, fuzzy=True)
#             last_date = ldt.date()
#
#             date_list = models.Date.objects.values('event_id').filter(event_date__range=[first_date, last_date])\
#                 .distinct()
#
#             for date in date_list:
#                 event = models.Event.objects.get(pk=date['event_id'])
#                 # if event.create_date == update_date:
#                 return_list.append(get_event_dict(event))
#
#     n = json.dumps(return_list)
#     json_string = '{"Dates" : %s}' % n
#
#     return HttpResponse(json_string)
# # "show": ,
# # "artist_event": {"id": , "name": ""},
# # "price": [{"price": , "id": }, ...],
# # "sellout": ,
# # "venue": {"id": , "name": ""},
# # "sale": ,
# #  "rank": ,
# # "promoter": [{"id": , "name": ""}, ...],
# # "id": },
#
#
# def isSameObject(event1, event2):
#     # print('%s / %s' %(event1.id, event2.id))
#     if event1.artist_event_id == event2.artist_event_id \
#             and event1.venue_id == event2.venue_id\
#             and event1.city_id == event2.city_id\
#             and event1.dates == event2.dates:
#         return True
#     else:
#         return False
#
#
# def get_distinct_event_list(event_list):
#     return_dict = list()
#
#     index1 = 0
#     while index1 < len(event_list):
#         index2 = index1+1
#         same_flag = False
#         while index2 < len(event_list):
#             same_flag = isSameObject(event_list[index1], event_list[index2])
#             if same_flag:
#                 break
#
#             index2 += 1
#
#         if not same_flag:
#             return_dict.append(get_event_dict(event_list[index1]))
#         index1 += 1
#
#     return return_dict
#
#
# # return event dictionary
#
# def get_event_dict(event):
#     event_dict = model_to_dict(event)
#
#     artist = models.ArtistEvent.objects.get(pk=event.artist_event_id)
#     event_dict.update({"artist_event": model_to_dict(artist)})
#
#     venue = models.Venue.objects.get(pk=event.venue_id)
#     event_dict.update({"venue": model_to_dict(venue)})
#
#     city = models.City.objects.get(pk=event.city_id)
#     event_dict.update({"city": model_to_dict(city)})
#
#     promoter_obj_list = models.EventPromoter.objects.filter(event_id=event.id)
#     promoter_list = list()
#     for promoter_obj in promoter_obj_list:
#         promoter = models.Promoter.objects.get(pk=promoter_obj.promoter_id)
#         promoter_list.append(model_to_dict(promoter))
#
#     event_dict.update({"promoter": promoter_list})
#
#     price_obj_list = models.EventPrice.objects.filter(event_id=event.id)
#     price_list = list()
#     for price_obj in price_obj_list:
#         price = models.Price.objects.get(pk=price_obj.price_id)
#         price_list.append(model_to_dict(price))
#
#     event_dict.update({"price": price_list})
#
#     return event_dict
