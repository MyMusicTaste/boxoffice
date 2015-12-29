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


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^boxoffice/date/$', 'django_boxoffice.boxoffice_app.views.get_date'),
    # url(r'^boxoffice/date/(?P<sdate>[0-9]+)/$', 'django_boxoffice.boxoffice_app.views.get_date'),
    # url(r'^boxoffice/date/(?P<sdate>[0-9]+)/(?P<ldate>[0-9]+)/$', 'django_boxoffice.boxoffice_app.views.get_date'),

    # url(r'^boxoffice/artist/$', 'django_boxoffice.boxoffice_app.views.get_artist_event'),
    # url(r'^boxoffice/artist/(?P<artist_id>\d+)/$', 'django_boxoffice.boxoffice_app.views.get_artist_event'),
    # url(r'^boxoffice/promoter/$', 'django_boxoffice.boxoffice_app.views.get_promoter'),
    # url(r'^boxoffice/promoter/(?P<promoter_id>\d+)/$', 'django_boxoffice.boxoffice_app.views.get_promoter'),
    #
    # url(r'^boxoffice/event/$', 'django_boxoffice.boxoffice_app.views.get_event'),
    # url(r'^boxoffice/event/(?P<param_id>\d+)/$', 'django_boxoffice.boxoffice_app.views.get_event'),
    # url(r'^boxoffice/event/(?P<parameter>[a-z]+)/(?P<param_id>\d+)/$', 'django_boxoffice.boxoffice_app.views.get_event'),

    url(r'^boxoffice/artists/$', 'django_boxoffice.boxoffice_app.views.get_artists'),
    url(r'^boxoffice/artists/(?P<artist_id>\d+)/$', 'django_boxoffice.boxoffice_app.views.get_artists'),
    url(r'^boxoffice/artists/(?P<artist_id>\d+)/event/$', 'django_boxoffice.boxoffice_app.views.get_artist_event2'),

]
