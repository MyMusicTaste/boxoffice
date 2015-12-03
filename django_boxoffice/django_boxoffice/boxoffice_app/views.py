# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import models
import json
import datetime
from dateutil import parser
from django.forms.models import model_to_dict

# Create your views here.

# return json : {"Date" : [{"event_id":"", "event_date":""}, ...]}
def get_date(request, sdate=None, ldate=None):
    return_list = list()

    if sdate is None:
        date_list = models.Date.objects.all()

        return_list = list()
        for date in date_list:
            date_dict = {"event_id": date.event_id, "event_date": date.event_date.strftime("%Y-%m-%d")}
            return_list.append(date_dict)

    else:
        default_date = datetime.datetime(datetime.MINYEAR, 1, 1)
        sdt = parser.parse(sdate, default=default_date, fuzzy=True)
        first_date = sdt.date()

        if ldate is None:

            date_list = models.Date.objects.filter(event_date__gte=first_date)

            for date in date_list:
                date_dict = {"event_id": date.event_id, "event_date": date.event_date.strftime("%Y-%m-%d")}
                return_list.append(date_dict)

        else:
            ldt = parser.parse(ldate, default=default_date, fuzzy=True)
            last_date = ldt.date()

            date_list = models.Date.objects.filter(event_date__range=[first_date, last_date]).\
                values('event_id', 'event_date').distinct()

            return_list = list()
            for date in date_list:
                date['event_date'] = date['event_date'].strftime("%Y-%m-%d")
                return_list.append(date)

    n = json.dumps(return_list)
    json_string = '{"Dates : %s}' % n

    return HttpResponse(json_string)


# return json : {"ArtistEvent" : [{"id":"", "artist_event":""}, ...]}
def get_artist_event(request, artist_id=0):
    return_dict = list()

    if artist_id == 0:
        array = models.ArtistEvent.objects.all()
        for artist in array:
            return_dict.append({"id": artist.id, "name": artist.name})
    else :
        artist = models.ArtistEvent.objects.get(pk=artist_id)
        return_dict.append({"id": artist.id, "name": artist.name})

    n = json.dumps(return_dict)
    json_string = '{"ArtistEvent" : %s}' % n
    return HttpResponse(json_string)


# return json : {"Promoter" : [{"id":"", "promoter":""}, ...]}
def get_promoter(request, promoter_id=0):
    return_dict = list()

    if promoter_id == 0:
        array = models.Promoter.objects.all()
        for promoter in array:
            return_dict.append({"id": promoter.id, "name": promoter.name})
    else :
        promoter = models.Promoter.objects.get(pk=promoter_id)
        return_dict.append({"id": promoter.id, "name": promoter.name})

    n = json.dumps(return_dict)
    json_string = '{"Promoter" : %s}' % n
    return HttpResponse(json_string)


# return json :
# {"Event" :
# [{"city": {"state": "", "id":, "name": ""},
#  "dates": "",
# "capacity": ,
# "attend": ,
# "show": ,
# "artist_event": {"id": , "name": ""},
# "price": [{"price": , "id": }, ...],
# "sellout": ,
# "venue": {"id": , "name": ""},
# "sale": ,
#  "rank": ,
# "promoter": [{"id": , "name": ""}, ...],
# "id": },
def get_event(request, parameter=None, param_id=None):
    return_dict = list()

    if parameter == None:
        if param_id == None:
            event_list = models.Event.objects.all()
            for event in event_list:
                return_dict.append(get_event_dict(event))
        else:
            event = models.Event.objects.get(pk=param_id)
            return_dict.append(get_event_dict(event))

    else:
        if parameter == "artist":
            event_list = models.Event.objects.filter(artist_event_id=param_id)
            for event in event_list:
                return_dict.append(get_event_dict(event))

        elif parameter == 'venue':
            event_list = models.Event.objects.filter(venue_id=param_id)
            for event in event_list:
               return_dict.append(get_event_dict(event))
        elif parameter == 'city':
            event_list = models.Event.objects.filter(city_id=param_id)
            for event in event_list:
               return_dict.append(get_event_dict(event))
        elif parameter == 'promoter':
            promoter_list = models.EventPromoter.objects.filter(promoter_id=param_id)
            for event_promoter in promoter_list:
                event_list = models.Event.objects.filter(id=event_promoter.event_id)
                for event in event_list:
                    return_dict.append(get_event_dict(event))


    n = json.dumps(return_dict)
    json_string = '{"Event" : %s}' % n
    return HttpResponse(json_string)


# return event dictionary
def get_event_dict(event):
    event_dict = model_to_dict(event)

    artist = models.ArtistEvent.objects.get(pk=event.artist_event_id)
    event_dict.update({"artist_event": model_to_dict(artist)})

    venue = models.Venue.objects.get(pk=event.venue_id)
    event_dict.update({"venue": model_to_dict(venue)})

    city = models.City.objects.get(pk=event.city_id)
    event_dict.update({"city": model_to_dict(city)})

    promoter_obj_list = models.EventPromoter.objects.filter(event_id=event.id)
    promoter_list = list()
    for promoter_obj in promoter_obj_list:
        promoter = models.Promoter.objects.get(pk=promoter_obj.promoter_id)
        promoter_list.append(model_to_dict(promoter))

    event_dict.update({"promoter": promoter_list})

    price_obj_list = models.EventPrice.objects.filter(event_id=event.id)
    price_list = list()
    for price_obj in price_obj_list:
        price = models.Price.objects.get(pk=price_obj.price_id)
        price_list.append(model_to_dict(price))

    event_dict.update({"price": price_list})

    return event_dict