from django.db import models


# Create your models here.
class ArtistEvent(models.Model):
    # id = models.AutoField( primary_key=True)
    name = models.CharField(max_length=512)

    class Admin:
        pass

    def __unicode__(self):
        return self.name


class City(models.Model):
    # id = models.AutoField( primary_key=True)
    name = models.CharField(max_length=256)
    state = models.CharField(max_length=256)

    class Admin:
        pass

    def __unicode__(self):
        return "%s, %s" % (self.name, self.state)

class Venue(models.Model):
    # id = models.AutoField( primary_key=True)
    name = models.CharField(max_length=256)

    class Admin:
        pass


class Price(models.Model):
    # id = models.AutoField( primary_key=True)
    price = models.FloatField()

    class Admin:
        pass


class Promoter(models.Model):
    # id = models.AutoField( primary_key=True)
    name = models.CharField(max_length=256)

    class Admin:
        pass


class Event(models.Model):
    # id = models.AutoField( primary_key=True)
    artist_event = models.ForeignKey(ArtistEvent)
    city = models.ForeignKey(City)
    venue = models.ForeignKey(Venue)
    sale = models.FloatField()
    attend = models.IntegerField()
    capacity = models.IntegerField()
    show = models.IntegerField()
    sellout = models.IntegerField()
    rank = models.IntegerField()
    dates = models.CharField(max_length=512)

    class Admin:
        pass


class EventPromoter(models.Model):
    class Meta:
        unique_together = (('event', 'promoter'),)
    # id = models.AutoField( primary_key=True)
    event = models.ForeignKey(Event)
    promoter = models.ForeignKey(Promoter)

    class Admin:
        pass


class EventPrice(models.Model):
    class Meta:
        unique_together = (('event', 'price'),)
    # id = models.AutoField( primary_key=True)
    event = models.ForeignKey(Event)
    price = models.ForeignKey(Price)

    class Admin:
        pass


class Date(models.Model):
    class Meta:
        unique_together = (('event', 'year', 'month', 'date'),)
    # id = models.AutoField( primary_key=True)
    event = models.ForeignKey(Event)
    year = models.IntegerField()
    month = models.IntegerField()
    date = models.IntegerField()

    class Admin:
        pass


class ErrorLog(models.Model):
    # id = models.AutoField( primary_key=True)
    table_name = models.CharField(max_length=256)
    artist_event = models.CharField(max_length=512)
    city = models.CharField(max_length=256)
    venue = models.CharField(max_length=256)
    attend_capacity = models.CharField(max_length=256)
    gross_sales = models.CharField(max_length=256)
    show_sellout = models.CharField(max_length=256)
    rank = models.CharField(max_length=256)
    dates = models.CharField(max_length=512)
    prices = models.CharField(max_length=256)
    promoters = models.CharField(max_length=512)

    class Admin:
        pass

