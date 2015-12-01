# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import Event

# Create your views here.
def index(request, page='default'):
    return HttpResponse('Page test %s' % page)

def getArtist_Event(request):
    array = Event.objects.all()
    return HttpResponse("test : %s" % array)