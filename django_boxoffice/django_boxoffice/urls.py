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

    url(r'^boxoffice/artists/$', 'django_boxoffice.boxoffice_app.views.get_artists'),
    url(r'^boxoffice/artists/(?P<id_numb>\d+)/$', 'django_boxoffice.boxoffice_app.views.get_artists'),
    url(r'^boxoffice/artists/(?P<id_numb>\d+)/events/$', 'django_boxoffice.boxoffice_app.views.get_artist_event'),

    url(r'^boxoffice/promoters/$', 'django_boxoffice.boxoffice_app.views.get_promoters'),
    url(r'^boxoffice/promoters/(?P<id_numb>\d+)/$', 'django_boxoffice.boxoffice_app.views.get_promoters'),
    url(r'^boxoffice/promoters/(?P<id_numb>\d+)/events/$', 'django_boxoffice.boxoffice_app.views.get_promoter_event'),

    url(r'^boxoffice/cities/$', 'django_boxoffice.boxoffice_app.views.get_cities'),
    url(r'^boxoffice/cities/(?P<id_numb>\d+)/$', 'django_boxoffice.boxoffice_app.views.get_cities'),
    url(r'^boxoffice/cities/(?P<id_numb>\d+)/events/$', 'django_boxoffice.boxoffice_app.views.get_city_event'),

    url(r'^boxoffice/events/$', 'django_boxoffice.boxoffice_app.views.get_events'),
    url(r'^boxoffice/events/(?P<id_numb>\d+)/$', 'django_boxoffice.boxoffice_app.views.get_events'),

    # url(r'^boxoffice/event_date/$', 'django_boxoffice.boxoffice_app.views.get_event_dates'),
    # url(r'^boxoffice/event_start_date/(?P<s_date>[0-9]+)/$', 'django_boxoffice.boxoffice_app.views.get_event_dates'),
    # url(r'^boxoffice/event_start_date/(?P<s_date>[0-9]+)/end_date/(?P<e_date>[0-9]+)/$', 'django_boxoffice.boxoffice_app.views.get_event_dates'),
]
