# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import models
import json
import datetime
from dateutil import parser
from django.db.models.query import QuerySet
from models import Date


# Create your views here.

def get_date(request, sdate=None, ldate=None):

    if sdate is None:
        array = models.Date.objects.all()
        return_list = list()
        for date in array:
            date_dict = dict()
            date_dict.update({'event_id': date.event_id, 'year': date.year, 'month': date.month, 'date': date.date})
            return_list.append(date_dict)

        n = json.dumps(return_list)
        json_string = '{"Date" : %s}' % n
        return HttpResponse(json_string)

    DEFAULT_DATE = datetime.datetime(datetime.MINYEAR, 1, 1)
    sdt = parser.parse(sdate, default=DEFAULT_DATE, fuzzy=True)

    if ldate is None:
        arr = models.Date.objects.filter(year__gte=int(sdt.year)).\
            filter(month__gte=sdt.month).\
            filter(date__gte=sdt.day)

        return HttpResponse('year:%s, month:%s, date:%s'
                            % (sdt.year, sdt.month, sdt.day))
    else:
        ldt = parser.parse(ldate, default=DEFAULT_DATE, fuzzy=True)

        first_date = sdt.date()
        last_date = ldt.date()

        arr = models.Date.objects.filter(event_date__range=[first_date, last_date])
        # , '%s-%s-%s' % (ldt.year, ldt.month, ldt.day)


        for date in arr:
            print(date.event_date)

        return HttpResponse('year:%s, month:%s, date:%s - year:%s, month:%s, date:%s'
                            % (sdt.year, sdt.month, sdt.day, ldt.year, ldt.month, ldt.day))


def get_artist_event(request, artist_id=0):
    return_dict = dict()

    if artist_id == 0:
        array = models.ArtistEvent.objects.all()
        for artist in array:
            return_dict.update({artist.id: artist.name})
    else :
        artist = models.ArtistEvent.objects.get(pk=artist_id)
        return_dict.update({artist.id: artist.name})

    n = json.dumps(return_dict)
    json_string = '{"ArtistEvent" : %s}' % n
    return HttpResponse(json_string)


def get_promoter(request, promoter_id=0):
    return_dict = dict()

    if promoter_id == 0:
        array = models.Promoter.objects.all()
        for promoter in array:
            return_dict.update({promoter.id: promoter.name})
    else :
        promoter = models.Promoter.objects.get(pk=promoter_id)
        return_dict.update({promoter.id: promoter.name})

    n = json.dumps(return_dict)
    json_string = '{"Promoter" : %s}' % n
    return HttpResponse(json_string)
