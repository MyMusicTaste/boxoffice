"""django_boxoffice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^boxoffice/artists/$', 'boxoffice_app.views.get_artists'),
    url(r'^boxoffice/artists/(?P<id_numb>\d+)/$', 'boxoffice_app.views.get_artists'),
    url(r'^boxoffice/artists/(?P<id_numb>\d+)/events/$', 'boxoffice_app.views.get_artist_event'),

    url(r'^boxoffice/promoters/$', 'boxoffice_app.views.get_promoters'),
    url(r'^boxoffice/promoters/(?P<id_numb>\d+)/$', 'boxoffice_app.views.get_promoters'),
    url(r'^boxoffice/promoters/(?P<id_numb>\d+)/events/$', 'boxoffice_app.views.get_promoter_event'),

    url(r'^boxoffice/cities/$', 'boxoffice_app.views.get_cities'),
    url(r'^boxoffice/cities/(?P<id_numb>\d+)/$', 'boxoffice_app.views.get_cities'),
    url(r'^boxoffice/cities/(?P<id_numb>\d+)/events/$', 'boxoffice_app.views.get_city_event'),

    url(r'^boxoffice/events/$', 'boxoffice_app.views.get_events'),
    url(r'^boxoffice/events/(?P<id_numb>\d+)/$', 'boxoffice_app.views.get_events'),

    # url(r'^boxoffice/event_date/$', 'django_boxoffice.boxoffice_app.views.get_event_dates'),
    # url(r'^boxoffice/event_start_date/(?P<s_date>[0-9]+)/$', 'django_boxoffice.boxoffice_app.views.get_event_dates'),
    # url(r'^boxoffice/event_start_date/(?P<s_date>[0-9]+)/end_date/(?P<e_date>[0-9]+)/$', 'django_boxoffice.boxoffice_app.views.get_event_dates'),

    url(r'^bookingAgent/clients/$', 'booking_app.views.get_clients'),
    url(r'^bookingAgent/clients/(?P<id_numb>\d+)/$', 'booking_app.views.get_clients'),
    url(r'^bookingAgent/clients/(?P<id_numb>\d+)/representatives/$', 'booking_app.views.get_client_representatives'),

    url(r'^bookingAgent/representatives/$', 'booking_app.views.get_representatives'),
    url(r'^bookingAgent/representatives/(?P<id_numb>\d+)/$', 'booking_app.views.get_representatives'),
    url(r'^bookingAgent/representatives/(?P<id_numb>\d+)/clients/$', 'booking_app.views.get_representatives_client'),

    url(r'^bookingAgent/clients_representatives/$', 'booking_app.views.get_clients_representatives'),
    url(r'^bookingAgent/clients_representatives/(?P<id_numb>\d+)/$', 'booking_app.views.get_clients_representatives'),
]
